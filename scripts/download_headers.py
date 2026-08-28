#!/usr/bin/env python3
"""下載並轉換header橫幅圖為WebP"""
import os
import urllib.request
from PIL import Image
import io

IMG_DIR = r"C:\Users\SUSI\Doubao\chats\2026-08-27\new-chat-18\petlogic-org\images"

BANNERS = {
    "header-default.webp": "https://aka.doubaocdn.com/s/mmCu2Kjkzo",
    "header-cat-behavior.webp": "https://aka.doubaocdn.com/s/gsmWijRsXh",
    "header-dog-training.webp": "https://aka.doubaocdn.com/s/L0Hkqqokzf",
    "header-pet-nutrition.webp": "https://aka.doubaocdn.com/s/V6jemZMUDP",
    "header-senior-pet.webp": "https://aka.doubaocdn.com/s/GZiaHQxvnV",
    "header-puppy-kitten.webp": "https://aka.doubaocdn.com/s/byDlaJIGlV",
    "header-exotic-pets.webp": "https://aka.doubaocdn.com/s/ZiUVrUQFdr",
    "header-pets-city.webp": "https://aka.doubaocdn.com/s/SxxOUJRPKI",
    "header-pet-culture.webp": "https://aka.doubaocdn.com/s/cE8iRxTPKW",
    "header-pet-product.webp": "https://aka.doubaocdn.com/s/qG8moxbLU2",
}

os.makedirs(IMG_DIR, exist_ok=True)

for fname, url in BANNERS.items():
    path = os.path.join(IMG_DIR, fname)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        img = Image.open(io.BytesIO(data))
        # 調整尺寸為1920x400
        img = img.convert("RGB")
        img = img.resize((1920, 400), Image.LANCZOS)
        img.save(path, "WEBP", quality=82)
        size_kb = os.path.getsize(path) / 1024
        print(f"  ✓ {fname}: {img.size[0]}x{img.size[1]}, {size_kb:.0f}KB")
    except Exception as e:
        print(f"  ✗ {fname}: {e}")

print(f"\n完成: {len(BANNERS)} 張header橫幅圖")
