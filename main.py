import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.data import personal_info, education_timeline, career_timeline, projects, news, contact_info

app = FastAPI(title="Personal Portfolio - Industrial Automation Engineer")

# Mount static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "app", "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "app", "templates")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Setup templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {
        "request": request,
        "page": "home",
        "personal": personal_info
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/education", response_class=HTMLResponse)
async def education(request: Request):
    context = {
        "request": request,
        "page": "education",
        "timeline": education_timeline
    }
    return templates.TemplateResponse("education.html", context)

@app.get("/career", response_class=HTMLResponse)
async def career(request: Request):
    context = {
        "request": request,
        "page": "career",
        "timeline": career_timeline,
        "projects": projects
    }
    return templates.TemplateResponse("career.html", context)

@app.get("/news", response_class=HTMLResponse)
async def news_page(request: Request):
    context = {
        "request": request,
        "page": "news",
        "news": news
    }
    return templates.TemplateResponse("news.html", context)

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    context = {
        "request": request,
        "page": "contact",
        "contact": contact_info
    }
    return templates.TemplateResponse("contact.html", context)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)