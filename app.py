# app.py - FastAPI Backend
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io
from inference import generate_caption

app = FastAPI(title="Image Captioning API")

# CORS ayarları (frontend'den erişim için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Image Captioning API - POST /caption endpoint'ine resim yükleyin"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/caption")
async def caption_image(file: UploadFile = File(...)):
    """Yüklenen resim için açıklama üretir"""
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    caption = generate_caption(image)
    return {"caption": caption, "filename": file.filename}
