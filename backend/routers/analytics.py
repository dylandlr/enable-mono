from fastapi import APIRouter, Depends
from backend.deps import require_role

router = APIRouter()

@router.get("/")
def get_analytics(role: str = Depends(require_role(['Admin']))):
    return {"analytics": {}, "role": role}

@router.get("/analytics/progress")
def get_progress_analytics(role: str = Depends(require_role(['Admin', 'Teacher']))):
    # TODO: Aggregate progress from Redis for all students
    from redis import Redis
    import os
    REDIS_URL = os.getenv("REDIS_URL") or os.getenv("KV_URL")
    redis_client = Redis.from_url(REDIS_URL) if REDIS_URL else None
    if not redis_client:
        return {"error": "Redis not configured"}
    student_ids = redis_client.smembers("analytics:active_students")
    progress = {sid.decode(): int(redis_client.get(f"analytics:progress:{sid.decode()}")) for sid in student_ids}
    return {"progress": progress}
