from fastapi import File, UploadFile, Request, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.minersFuncs import alpha_model
import base64
import pm4py
import os
from PIL import Image


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="UI-template",auto_reload=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/submit")
def upload(request: Request, file: UploadFile = File(...)):
    os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
    try:
        contents = file.file.read()
      
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
  
    model = alpha_model("app/repairExample.xes")
    return templates.TemplateResponse("main.html", {"request": request,  "myImage": model})

# @app.get("/")
# def main(request: Request):
#     return templates.TemplateResponse("index.html", {"request": request})
  
# @app.post("/upload")
# def upload(request: Request, file: UploadFile = File(...)):
#     os.environ["PATH"] +=os.pathsep + 'C:/Program Files (x86)/Graphviz/bin/'
#     try:
#         contents = file.file.read()
        
#     except Exception:
#         return {"message": "There was an error uploading the file"}
#     finally:
#         file.file.close()
    
#     model = alpha_model("app/repairExample.xes")
#     return templates.TemplateResponse("index.html", {"request": request,  "myImage": model})