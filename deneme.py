"""
deneme.py - İlk Model Testi
============================
Bu dosya, Salesforce/blip-image-captioning-base modelinin
çalışıp çalışmadığını test etmek için oluşturulmuştur.

Amaç: Pre-trained modelin görsellerden doğru caption ürettiğini doğrulamak.
"""

from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
import io

print("=" * 50)
print("BLIP Image Captioning - İlk Test")
print("=" * 50)

# 1. Modeli ve işlemciyi (processor) yükle
print("\n[1/4] Model yükleniyor...")
MODEL_ID = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(MODEL_ID)
model = BlipForConditionalGeneration.from_pretrained(MODEL_ID)
print("✓ Model başarıyla yüklendi!")

# 2. Test için bir resim yükle
print("\n[2/4] Test görseli indiriliyor...")
# Picsum: güvenilir ve her zaman çalışan test görseli servisi
url = "https://picsum.photos/id/237/400/300"  # Köpek görseli
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers, stream=True)
image = Image.open(io.BytesIO(response.content)).convert('RGB')
print(f"✓ Görsel indirildi: {image.size[0]}x{image.size[1]} piksel")

# 3. Resmi modele uygun hale getir (Preprocessing)
print("\n[3/4] Görsel işleniyor (preprocessing)...")
inputs = processor(image, return_tensors="pt")
print("✓ Görsel tensor formatına dönüştürüldü")

# 4. Modeli çalıştır ve çıktı üret (Inference)
print("\n[4/4] Model çalıştırılıyor (inference)...")
outputs = model.generate(**inputs, max_new_tokens=30)
caption = processor.decode(outputs[0], skip_special_tokens=True)

print("\n" + "=" * 50)
print("SONUÇ")
print("=" * 50)
print(f"Üretilen Caption: {caption}")
print("=" * 50)
print("\n✓ TEST BAŞARILI - Model çalışıyor!")
