#routers/auth.py
from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from database import get_db_connection
import hashlib
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/auth')
templates = Jinja2Templates(directory="templates")

@router.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# 회원가입
@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    connection = get_db_connection()
    cursor = connection.cursor()

    # 비밀번호 해시
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, hashed_password)
        )
        connection.commit()
        return RedirectResponse(url="/", status_code=303)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        connection.close()

# 로그인
@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    connection = get_db_connection()
    cursor = connection.cursor()

    # 비밀번호 해시
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s",
        (username, hashed_password)
    )
    user = cursor.fetchone()
    print(user)

    if user:
        return RedirectResponse(url="/", status_code=303)
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")