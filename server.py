from fastapi import FastAPI, Request, UploadFile, status
from fastapi.params import File
from fastapi.datastructures import UploadFile
from fastapi.templating import Jinja2Templates
from starlette.background import BackgroundTasks
import main
from starlette.requests import Request
from fastapi.responses import FileResponse
import shutil
import main
import os
# import ocr
# import requests
# from pydantic import BaseModel
# from typing import List
# from pymongo import MongoClient
# import motor.motor_asyncio
import logging
from fastapi.staticfiles import StaticFiles


# mongo_url = "mongodb+srv://admin-kushagra:kushagra@cluster0.imgaq.mongodb.net/TextDB?retryWrites=true&w=majority"
# client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
# db = client["TextDB"]
# collection = db["Files"]



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

templates = Jinja2Templates(directory='templates')

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.post('/upload')
async def perform_ocr(file: UploadFile = File(...)):
    filename = file.filename[0:len(file.filename)-4]
    temp_file = _save_file_to_disk(file, path="PDFs", save_as= filename)
    main.final()
    return temp_file
    # text = ocr.pdfToTxt(temp_file)
    # return {"filename": file.filename, "text": text}
    

@app.post('/bulk_extract_text')
async def bulk_perform_ocr(request: Request, bg_tasks: BackgroundTasks):
    files = await request.form()

    folder_name = "PDFs"
    
    for file in files.values():
        filename = file.filename[0:len(file.filename)-4]
        temp_file = _save_file_to_disk(file, path = folder_name, save_as = filename)
    main.final()
    return
    


def _save_file_to_disk(uploaded_file, path=".", save_as="default"):
    extension = os.path.splitext(uploaded_file.filename)[-1]
    temp_file = os.path.join(path, save_as + extension)
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)
    return temp_file

@app.get('/download')
def download_file():
    return FileResponse("mergedInvoice/A.xlsx")

    
    
#     text = collection.find_one({"file_name" : "Output.txt"})
#     print(text)

    
    