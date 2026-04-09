from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(title="Personal Portfolio - Industrial Automation Engineer")

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = {
        "request": request,
        "page": "home"
    }
    return templates.TemplateResponse("index.html", context)

@app.get("/education", response_class=HTMLResponse)
async def education(request: Request):
    context = {
        "request": request,
        "page": "education"
    }
    return templates.TemplateResponse("education.html", context)

@app.get("/career", response_class=HTMLResponse)
async def career(request: Request):
    context = {
        "request": request,
        "page": "career"
    }
    return templates.TemplateResponse("career.html", context)

@app.get("/news", response_class=HTMLResponse)
async def news(request: Request):
    context = {
        "request": request,
        "page": "news"
    }
    return templates.TemplateResponse("news.html", context)

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    context = {
        "request": request,
        "page": "contact"
    }
    return templates.TemplateResponse("contact.html", context)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)