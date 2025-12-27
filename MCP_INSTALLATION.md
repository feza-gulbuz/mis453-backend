# MCP Server Installation Guide

## 🤖 Image Captioning MCP Server

Bu MCP sunucusu, Claude Desktop ve diğer AI agent'larının Image Captioning API'sine erişmesini sağlar.

## 📦 Kurulum

### 1. Bağımlılıkları Yükleyin

```bash
pip install fastmcp requests pillow
```

### 2. MCP Sunucusunu İndirin

```bash
git clone https://github.com/feza-gulbuz/mis453-backend.git
cd mis453-backend
```

### 3. Claude Desktop Konfigürasyonu

Claude Desktop config dosyasını düzenleyin:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Aşağıdaki konfigürasyonu ekleyin:

```json
{
    "mcpServers": {
        "image-captioning": {
            "command": "python",
            "args": ["/path/to/mis453-backend/mcp_server.py"]
        }
    }
}
```

> ⚠️ `/path/to/` kısmını gerçek dosya yolu ile değiştirin!

### 4. Claude Desktop'ı Yeniden Başlatın

Konfigürasyonu kaydetdikten sonra Claude Desktop'ı kapatıp tekrar açın.

## 🔧 Kullanılabilir Fonksiyonlar

### `caption_image_from_url(image_url: str)`
Bir URL'den görsel indirir ve AI ile açıklama üretir.

**Örnek:**
```
"https://example.com/photo.jpg" adresindeki görseli analiz et
```

### `caption_image_from_base64(image_base64: str)`
Base64 formatındaki görsel için açıklama üretir.

### `get_api_status()`
API'nin çalışıp çalışmadığını kontrol eder.

## 🧪 Test

MCP sunucusunu test etmek için:

```bash
python mcp_server.py
```

## 📡 API Endpoint

MCP sunucusu şu API'yi kullanır:
- **URL:** https://fzaaa-mis453-backend.hf.space
- **Endpoint:** POST /caption

## 📄 License

MIT License
