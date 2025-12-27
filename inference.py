"""
inference.py - Core ML Logic (Çekirdek Makine Öğrenmesi Mantığı)
================================================================
Bu dosya, projenin CORE bileşenidir.
Diğer tüm bileşenler (API, Frontend, MCP) bu dosyayı kullanır.

Model: Salesforce/blip-image-captioning-base
Girdi: PIL Image objesi
Çıktı: String (görsel açıklaması)
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from typing import Optional

# Model ayarları
MODEL_ID = "Salesforce/blip-image-captioning-base"

# Global değişkenler (model bir kez yüklenir)
_processor = None
_model = None

def load_model():
    """Modeli belleğe yükler (lazy loading)"""
    global _processor, _model
    
    if _processor is None or _model is None:
        print("[inference.py] Model yükleniyor...")
        _processor = BlipProcessor.from_pretrained(MODEL_ID)
        _model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)
        print("[inference.py] ✓ Model hazır!")
    
    return _processor, _model

def generate_caption(image: Image.Image, max_tokens: int = 30) -> str:
    """
    Verilen görsel için açıklama (caption) üretir.
    
    Args:
        image: PIL Image objesi
        max_tokens: Maksimum üretilecek kelime sayısı
    
    Returns:
        str: Görselin açıklaması (İngilizce)
    
    Örnek:
        >>> from PIL import Image
        >>> img = Image.open("kedi.jpg")
        >>> caption = generate_caption(img)
        >>> print(caption)
        "a cat sitting on a couch"
    """
    processor, model = load_model()
    
    # Görseli RGB formatına çevir (bazı görseller RGBA olabilir)
    image = image.convert("RGB")
    
    # Preprocessing: görseli model için uygun formata dönüştür
    inputs = processor(image, return_tensors="pt")
    
    # Inference: modeli çalıştır
    outputs = model.generate(**inputs, max_new_tokens=max_tokens)
    
    # Postprocessing: tensor'ı string'e çevir
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

# Doğrudan çalıştırma testi
if __name__ == "__main__":
    import requests
    import io
    
    print("=" * 50)
    print("Inference Core - Test")
    print("=" * 50)
    
    # Test görseli - Picsum'dan güvenilir görsel
    url = "https://picsum.photos/id/237/400/300"  # Köpek
    print(f"\nTest URL: {url}")
    
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    image = Image.open(io.BytesIO(response.content))
    
    caption = generate_caption(image)
    
    print(f"\n✓ Sonuç: {caption}")
    print("=" * 50)
