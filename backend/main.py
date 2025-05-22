# Python backend for FastAPI

from fastapi import FastAPI, Request, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
import supabase
import os

# Import routers from routers package
from backend.routers.assignments import router as assignments_router
from backend.routers.analytics import router as analytics_router
from backend.routers.users import router as users_router
from backend.routers.lessons import router as lessons_router
from backend.routers.progress import router as progress_router

app = FastAPI()

# Allow CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI backend!"}

# --- OAUTH2/JWT CONFIG ---
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecret")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/token")

# --- SUPABASE CLIENT ---
SUPABASE_URL = os.getenv("SUPABASE_SUPABASE_URL") or os.getenv("SUPABASE_NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SUPABASE_SERVICE_ROLE_KEY")
sb = supabase.create_client(SUPABASE_URL, SUPABASE_KEY) if SUPABASE_URL and SUPABASE_KEY else None

# --- UTILS ---
def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    from datetime import datetime, timedelta
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- AUTH ROUTER ---
from fastapi import APIRouter

auth_router = APIRouter(prefix="/api/auth")

@auth_router.post("/signup")
def signup(form: OAuth2PasswordRequestForm = Depends()):
    # Check if user exists
    user = sb.table("users").select("*").eq("username", form.username).execute().data
    if user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = get_password_hash(form.password)
    # Insert user with default role 'Student'
    sb.table("users").insert({"username": form.username, "hashed_password": hashed, "role": "Student"}).execute()
    return {"msg": "User created"}

@auth_router.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = sb.table("users").select("*").eq("username", form.username).single().execute().data
    if not user or not verify_password(form.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token({"sub": user["username"], "role": user["role"]})
    return {"access_token": access_token, "token_type": "bearer"}

@auth_router.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        role = payload.get("role")
        if username is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username, "role": role}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# --- API Routing Standard ---
# All backend API endpoints are defined in modular FastAPI routers under backend/routers/.
# Each router (e.g., assignments.py, lessons.py) exposes endpoints under a logical prefix (e.g., /api/assignments, /api/lessons).
# The main.py mounts these routers with a /api prefix for all backend APIs.
# Frontend (Next.js) fetches data from /api/* endpoints, which are reverse-proxied to the backend FastAPI server in production (or via a proxy in dev).
# Next.js API routes (frontend/src/app/api/*) are reserved for frontend-only logic or edge functions, and should not duplicate backend business logic.
# All business logic, data access, and permissions enforcement must reside in the backend FastAPI routers.
# Example usage in main.py:
app.include_router(assignments_router, prefix="/api/assignments")
app.include_router(analytics_router, prefix="/api/analytics")
app.include_router(users_router, prefix="/api/users")
app.include_router(lessons_router, prefix="/api/lessons")
app.include_router(progress_router, prefix="/api")
app.include_router(auth_router)
