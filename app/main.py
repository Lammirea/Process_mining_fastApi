from fastapi import File, UploadFile, Request, FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.minersFuncs import *
import os
from fastapi.responses import FileResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="UI-template",auto_reload=True)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/file/downloadAlpha")
def upload_alpha(request: Request, file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        photo_path = os.path.join("buffer","alpha_"+file.filename)
        with open(photo_path, "wb") as f:
            f.write(contents)

        model = alpha_model(photo_path)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        os.remove(photo_path)
    
    return templates.TemplateResponse("main.html", {"request": request,  "myImage": model})

@app.post("/file/downloadInduct")
def upload_inductive(request: Request, file: UploadFile):
    try:
        contents = file.file.read()
        photo_path = os.path.join("buffer","inductive_"+file.filename)
        with open(photo_path, "wb") as f:
            f.write(contents)

        modelInduct = inductive_model(photo_path)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        os.remove(photo_path)
    
    return templates.TemplateResponse("main.html", {"request": request,  "myImage": modelInduct})

@app.post("/file/downloadHeuristics")
def upload_heuristics(request: Request, file: UploadFile):
    try:
        contents = file.file.read()
        photo_path = os.path.join("buffer","heuristics_"+file.filename)
        with open(photo_path, "wb") as f:
            f.write(contents)

        modelHeur = heuristics_model(photo_path)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        os.remove(photo_path)
    
    return templates.TemplateResponse("main.html", {"request": request,  "myImage": modelHeur})

@app.post("/file/downloadConformance")
def upload_conformance(request: Request, file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        photo_path = os.path.join("buffer","conformance_"+file.filename)
        with open(photo_path, "wb") as f:
            f.write(contents)

        modelConform = conformanceChecking(photo_path)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
        os.remove(photo_path)
    
    return templates.TemplateResponse("main.html", {"request": request,  "myImage": modelConform})



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
# @app.post("/file/downloadAlpha")
# def post_download_file():
#     __file__ = "app/repairExample.xes"    
#     return FileResponse(path=alpha_model(__file__), filename='petri_net_alpha.png', media_type='multipart/form-data')

# Загружает файл прямо на устройство
# @app.get("/file/downloadInduct")
# def download_file():
#   __file__ = "app/repairExample.xes"
#   return FileResponse(path=inductive_model(os.path.abspath(__file__)), filename='petri_net_induct.png', media_type='multipart/form-data')



