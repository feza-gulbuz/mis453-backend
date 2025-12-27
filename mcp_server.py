"""
MCP Server for Image Captioning API
====================================
Bu dosya, Claude Desktop ve diğer AI agent'larının
Image Captioning API'sine erişmesini sağlar.

Kurulum:
    pip install fastmcp requests pillow

Claude Desktop Konfigürasyonu (claude_desktop_config.json):
{
    "mcpServers": {
        "image-captioning": {
            "command": "python",
            "args": ["/path/to/mcp_server.py"]
        }
    }
}
"""

from fastmcp import FastMCP
import requests
import base64
import tempfile
import os

# MCP Server oluştur
mcp = FastMCP("Image Captioning MCP Server")

# API URL (Hugging Face deployment)
API_URL = "https://fzaaa-mis453-backend.hf.space/caption"

@mcp.tool()
def caption_image_from_url(image_url: str) -> str:
    """
    Bir URL'den görsel indirir ve açıklama üretir.
    
    Args:
        image_url: İnternetteki görselin URL'si
    
    Returns:
        Görselin AI tarafından üretilen açıklaması
    """
    try:
        # Görseli indir
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        # Geçici dosyaya kaydet
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            f.write(response.content)
            temp_path = f.name
        
        # API'ye gönder
        with open(temp_path, "rb") as f:
            files = {"file": ("image.jpg", f, "image/jpeg")}
            api_response = requests.post(API_URL, files=files, timeout=60)
        
        # Geçici dosyayı sil
        os.unlink(temp_path)
        
        if api_response.status_code == 200:
            return api_response.json()["caption"]
        else:
            return f"API Error: {api_response.status_code}"
            
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def caption_image_from_base64(image_base64: str, filename: str = "image.jpg") -> str:
    """
    Base64 encoded görsel için açıklama üretir.
    
    Args:
        image_base64: Base64 formatında encode edilmiş görsel
        filename: Dosya adı (varsayılan: image.jpg)
    
    Returns:
        Görselin AI tarafından üretilen açıklaması
    """
    try:
        # Base64'ü decode et
        image_data = base64.b64decode(image_base64)
        
        # Geçici dosyaya kaydet
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            f.write(image_data)
            temp_path = f.name
        
        # API'ye gönder
        with open(temp_path, "rb") as f:
            files = {"file": (filename, f, "image/jpeg")}
            api_response = requests.post(API_URL, files=files, timeout=60)
        
        # Geçici dosyayı sil
        os.unlink(temp_path)
        
        if api_response.status_code == 200:
            return api_response.json()["caption"]
        else:
            return f"API Error: {api_response.status_code}"
            
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_api_status() -> str:
    """
    Image Captioning API'nin durumunu kontrol eder.
    
    Returns:
        API'nin durumu (healthy/unhealthy)
    """
    try:
        response = requests.get(
            "https://fzaaa-mis453-backend.hf.space/health", 
            timeout=10
        )
        if response.status_code == 200:
            return "API is healthy and running"
        else:
            return f"API returned status code: {response.status_code}"
    except Exception as e:
        return f"API is not reachable: {str(e)}"

if __name__ == "__main__":
    # MCP sunucusunu başlat
    mcp.run()
