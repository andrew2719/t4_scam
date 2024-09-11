from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# In-memory storage for messages
messages = []

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/type", response_class=HTMLResponse)
async def type_page(request: Request):
    return templates.TemplateResponse("type.html", {"request": request})

@app.post("/type")
async def submit_message(message: str = Form(...)):
    messages.append(message)
    # Redirect back to the /type page after submitting the message
    return RedirectResponse(url="/type", status_code=303)

@app.get("/view", response_class=HTMLResponse)
async def view_page(request: Request):
    return templates.TemplateResponse("view.html", {"request": request, "messages": messages})
