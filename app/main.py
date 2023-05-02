from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json
from alphaMiner import *

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="UI-template",auto_reload=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    model = alpha_model("repairExample.xes")
    return templates.TemplateResponse("main.html", {"request": request , "data": model})
