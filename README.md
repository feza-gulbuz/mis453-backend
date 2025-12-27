# 🖼️ Image Captioning API (Backend)

A FastAPI-based backend service that generates captions for images using the BLIP model.

## 🚀 Features

- **Image Captioning**: Upload an image and get AI-generated descriptions
- **RESTful API**: Simple POST endpoint for image processing
- **BLIP Model**: Using Salesforce/blip-image-captioning-base

## 📁 Project Structure

```
backend/
├── app.py          # FastAPI application & API endpoints
├── inference.py    # Core ML logic (BLIP model integration)
├── eval.py         # Performance evaluation script
├── requirement.txt # Python dependencies
└── README.md       # This file
```

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/feza-gulbuz/mis453-backend.git
cd mis453-backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirement.txt
```

## ▶️ Running the Server

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## 📡 API Endpoints

### GET `/`
Health check endpoint.

**Response:**
```json
{"message": "Image Captioning API - POST /caption endpoint'ine resim yükleyin"}
```

### POST `/caption`
Upload an image to get a caption.

**Request:** `multipart/form-data` with `file` field

**Response:**
```json
{
  "caption": "a woman wearing a red dress",
  "filename": "image.jpg"
}
```

## 🧪 Testing

```bash
# Run evaluation script
python eval.py

# Test inference directly
python inference.py
```

## 📦 Dependencies

- FastAPI
- Uvicorn
- Transformers (BLIP model)
- Pillow
- PyTorch

## 📄 License

MIT License
