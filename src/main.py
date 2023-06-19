import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse, StreamingResponse
import os
from supabase import create_client, Client
from ultralytics import YOLO
from pydantic import BaseModel
import cv2
import base64

model = YOLO("best.pt")

arquivo = cv2.imread(filename="rachadura.jpg")

predicted = model.predict(source=arquivo, show=True, save=True)

app = FastAPI()
url: str = "https://yongpwmnossltvelyqjq.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inlvbmdwd21ub3NzbHR2ZWx5cWpxIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODcxOTI5ODIsImV4cCI6MjAwMjc2ODk4Mn0.kemzmS8_ykqlRg2UgZN3LvGSF2mFNmKhJGVZTfGCWgw"
supabase: Client = create_client(url, key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

table_name = "imagem"

schema_name = "public"

class imagem (BaseModel):
    id: int
    imagem: str

@app.post("/imagem")
async def images(request: Request):
    supabase=create_client(url,key)
    with open("runs/detect/predict/image0.jpg", 'rb+') as f:
        my_string = base64.b64encode(f.read()).decode('utf-8')

        response = supabase.table(table_name).insert({"imagem": my_string}).execute()
        print(response)
    return {"message": "Image uploaded successfully"}