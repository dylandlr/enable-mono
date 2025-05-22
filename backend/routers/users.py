from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from backend.deps import require_role

router = APIRouter()

@router.get("/")
def get_users(role: str = Depends(require_role(['Admin']))):
    return {"users": [], "role": role}

@router.post("/register")
def register_user(username: str, password: str, role: str = 'Student'):
    # TODO: Hash password, check for existing user, insert into DB
    return {"success": True, "message": "User registered (stub)"}

@router.post("/login")
def login_user(username: str, password: str):
    # TODO: Validate credentials, return session/token
    return {"success": True, "message": "User logged in (stub)"}

@router.get("/me")
def get_me(role: str = Depends(require_role(['Student', 'Teacher', 'Admin']))):
    # TODO: Return user info from session/token
    return {"user": {"username": "demo", "role": role}}
