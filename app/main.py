from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from app.minersFuncs import alpha_model
import base64

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="UI-template",auto_reload=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/createModel")
def upload(request: Request):
    model = alpha_model("app/repairExample.xes")
    base64_encoded_image = base64.b64encode(model).decode("utf-8")
    return templates.TemplateResponse("main.html", {"request": request,  "PetriNet":base64_encoded_image})
