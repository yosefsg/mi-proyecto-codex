from fastapi import FastAPI, Depends
from .auth import get_current_user

app = FastAPI(title="API Base con FastAPI + JWT")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/me")
def me(user: dict = Depends(get_current_user)):
    return {"user": user["username"]}
