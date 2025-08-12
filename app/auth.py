import time
from typing import Optional
from fastapi import HTTPException, Header
from jose import jwt

SECRET = "cambia-esto-en-produccion"  # Demo ONLY
ALGO = "HS256"

def create_token(username: str, exp_seconds: int = 3600) -> str:
    payload = {"username": username, "exp": int(time.time()) + exp_seconds}
    return jwt.encode(payload, SECRET, algorithm=ALGO)

def verify_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGO])
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

def extract_bearer(authorization: Optional[str]) -> str:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Falta Bearer token")
    return authorization.split(" ", 1)[1]

def get_current_user(authorization: Optional[str] = Header(None)):
    token = extract_bearer(authorization)
    payload = verify_token(token)
    return {"username": payload["username"]}
