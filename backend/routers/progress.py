from fastapi import APIRouter, Depends
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from backend.deps import require_role
from redis import Redis

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    from dotenv import load_dotenv
    load_dotenv()
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL environment variable not set. Please check your .env file and ensure it is loaded.")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

REDIS_URL = os.getenv("REDIS_URL") or os.getenv("KV_URL")
redis_client = Redis.from_url(REDIS_URL) if REDIS_URL else None

# Dummy fallback for demo if DB is not available
DUMMY_PROGRESS = 72
DUMMY_HISTORY = [
    {"date": "2025-05-15", "progress": 60},
    {"date": "2025-05-16", "progress": 62},
    {"date": "2025-05-17", "progress": 65},
    {"date": "2025-05-18", "progress": 68},
    {"date": "2025-05-19", "progress": 70},
    {"date": "2025-05-20", "progress": 72},
    {"date": "2025-05-21", "progress": 72},
]

router = APIRouter()  # Remove prefix here

@router.get("/progress/")
def get_progress(role: str = Depends(require_role(['Student']))):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT progress, message FROM student_progress WHERE student_id=1 ORDER BY updated_at DESC LIMIT 1"))
            row = result.fetchone()
            if row:
                return {"progress": row[0], "message": row[1]}
    except Exception:
        pass
    return {"progress": DUMMY_PROGRESS, "message": "You're on track! Keep it up!"}

@router.get("/progress/recommendations")
def get_recommendations(role: str = Depends(require_role(['Student']))):
    return {
        "links": [
            {"label": "Go to Lessons", "href": "/lessons"},
            {"label": "Track Your Progress", "href": "/progress"},
            {"label": "Practice in Playground", "href": "/playground"},
            {"label": "Ask the Support Agent", "href": "/chat"},
        ]
    }

@router.get("/progress/history")
def get_progress_history(role: str = Depends(require_role(['Student']))):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT date, progress FROM student_progress_history WHERE student_id=1 ORDER BY date ASC LIMIT 7"))
            history = [{"date": row[0].isoformat(), "progress": row[1]} for row in result.fetchall()]
            if history:
                return {"history": history}
    except Exception:
        pass
    return {"history": DUMMY_HISTORY}

@router.get("/progress/feedback")
def get_progress_feedback(role: str = Depends(require_role(['Student']))):
    return {
        "feedback": [
            "Great job keeping your progress steady!",
            "Try to complete overdue assignments for even better results.",
            "Explore new lessons to keep learning!"
        ]
    }

@router.post("/update")
def update_progress(
    lesson_id: int,
    increment: int = 1,
    user_id: int = 1,  # TODO: Replace with real user ID from auth
    role: str = Depends(require_role(['Student']))
):
    """
    Update student progress when a lesson is completed.
    - lesson_id: the completed lesson's ID
    - increment: how much to increment progress (default 1)
    - user_id: the student's user ID (should come from auth)
    """
    try:
        with engine.begin() as conn:
            # Log lesson completion
            conn.execute(
                text("""
                    INSERT INTO student_lesson_completion (student_id, lesson_id, completed_at)
                    VALUES (:student_id, :lesson_id, NOW())
                """),
                {"student_id": user_id, "lesson_id": lesson_id}
            )
            # Update progress
            conn.execute(
                text("""
                    UPDATE student_progress
                    SET progress = progress + :inc, updated_at = NOW()
                    WHERE student_id = :student_id
                """),
                {"inc": increment, "student_id": user_id}
            )
        # Track analytics in Redis
        if redis_client:
            redis_client.incrby(f"analytics:progress:{user_id}", increment)
            redis_client.sadd("analytics:active_students", user_id)
    except Exception as e:
        return {"success": False, "error": str(e)}
    return {"success": True}
