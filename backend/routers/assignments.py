from fastapi import APIRouter, Depends
from backend.deps import require_role

router = APIRouter()

@router.get("/")
def get_assignments(role: str = Depends(require_role(['Student', 'Teacher']))):
    return {"assignments": [], "role": role}
