from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ingest.video_ingest import process_youtube_video
from ingest.pdf_ingest import process_pdf
from models.rag import multimodal_query

import os

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload_video/")
async def upload_video(youtube_url: str = Form(...), query: str = Form(...)):
    # Process video
    doc_id = process_youtube_video(youtube_url)
    results = multimodal_query(doc_id, query)
    return {"results": results}

@app.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...), query: str = Form(...)):
    # Save uploaded PDF
    pdf_path = f"data/samples/{file.filename}"
    with open(pdf_path, "wb") as f:
        f.write(await file.read())
    doc_id = process_pdf(pdf_path)
    results = multimodal_query(doc_id, query)
    return {"results": results}
