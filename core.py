# core.py - Model ve Caption Üretme
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

MODEL_ID = "Salesforce/blip-image-captioning-base"

print("Model yükleniyor...")
processor = BlipProcessor.from_pretrained(MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)
print("Model yüklendi!")

def generate_caption(image: Image.Image) -> str:
    """Verilen resim için açıklama üretir"""
    image = image.convert("RGB")
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
