from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db_connection
from routers.auth import router as auth_router
import models

app = FastAPI()
templates = Jinja2Templates(directory="templates")

models.create_users_table()
#models.create_posts_table()

# 라우터 등록
app.include_router(auth_router)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


