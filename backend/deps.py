# backend/deps.py
from fastapi import Request, HTTPException, status, Depends

def get_role(request: Request) -> str:
    # Example: get role from header or cookie (replace with real auth logic)
    role = request.headers.get('X-User-Role') or request.cookies.get('role')
    if role in ['Student', 'Teacher', 'Admin']:
        return role
    return 'Student'  # Default fallback

def require_role(allowed_roles: list[str]):
    def dependency(request: Request):  # <-- should NOT be request: Request = Depends()
        role = get_role(request)
        if role not in allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized for this resource.")
        return role
    return dependency
