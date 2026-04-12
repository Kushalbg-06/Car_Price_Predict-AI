from fastapi import APIRouter
from app.db.supabase import supabase
from app.core.hash import verify_password
from app.core.security import create_access_token
from app.core.hash import hash_password

router = APIRouter()


@router.post("/signup")
def signup(username: str, password: str):

    hashed = hash_password(password)

    supabase.table("users").insert({
        "username": username,
        "password": hashed
    }).execute()

    return {"msg": "User created"}

@router.post("/login")
def login(username: str, password: str):

    # 🔍 1. Get user from database
    response = supabase.table("users").select("*").eq("username", username).execute()

    # ❌ If user not found
    if len(response.data) == 0:
        return {"error": "User not found"}

    user = response.data[0]

    # 🔐 2. Check password
    if not verify_password(password, user["password"]):
        return {"error": "Wrong password"}

    # 🎫 3. Create JWT token
    token = create_access_token({"sub": username})

    return {"access_token": token}