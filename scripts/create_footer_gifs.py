#!/usr/bin/env python3
"""
製作10個footer動畫GIF
Ken Burns效果：慢推/慢搖
"""
import os
import urllib.request
from PIL import Image

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "images")

# 10個主題的背景圖URL
THEMES = {
    "cat-behavior": "https://aka.doubaocdn.com/s/VA31WkTuQd",
    "dog-training": "https://aka.doubaocdn.com/s/qzb7gLGJbp",
    "pet-nutrition": "https://aka.doubaocdn.com/s/Js2K3j97GE",
    "senior-pet": "https://aka.doubaocdn.com/s/Vd8qoWuIel",
    "puppy-kitten": "https://aka.doubaocdn.com/s/WcYicoS4pN",
    "exotic-pets": "https://aka.doubaocdn.com/s/G5kh8dMni3",
    "pets-city": "https://aka.doubaocdn.com/s/IvHNldaxo1",
    "pet-culture": "https://aka.doubaocdn.com/s/0Sm3Dw5nqN",
    "pet-product": "https://aka.doubaocdn.com/s/VXet5kPdle",
    "default": "https://aka.doubaocdn.com/s/zahRrm2jh0",
}

FOOTER_W = 960
FOOTER_H = 150
FRAMES = 12  # 動畫幀數
DURATION = 150  # 每幀持續ms（總共約1.8秒循環）

def download_images():
    """下載10張背景圖"""
    os.makedirs(IMG_DIR, exist_ok=True)
    for name, url in THEMES.items():
        filepath = os.path.join(IMG_DIR, f"footer-bg-{name}.webp")
        if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
            print(f"  已存在: {name}")
            continue
        try:
            urllib.request.urlretrieve(url, filepath)
            print(f"  下載: {name}")
        except Exception as e:
            print(f"  失敗: {name} - {e}")

def create_gif(name):
    """製作單個動畫GIF（Ken Burns效果）"""
    src_path = os.path.join(IMG_DIR, f"footer-bg-{name}.webp")
    dst_path = os.path.join(IMG_DIR, f"footer-{name}.gif")
    
    if not os.path.exists(src_path):
        print(f"  缺少背景圖: {name}")
        return False
    
    img = Image.open(src_path).convert("RGB")
    w, h = img.size
    
    frames = []
    for i in range(FRAMES):
        # Ken Burns: 從1.0x慢慢放大到1.15x，同時輕微平移
        progress = i / (FRAMES - 1)
        scale = 1.0 + 0.12 * progress  # 1.0x -> 1.12x
        new_w = int(w * scale)
        new_h = int(h * scale)
        resized = img.resize((new_w, new_h), Image.LANCZOS)
        
        # 平移：從左側慢慢移到右側
        max_dx = new_w - FOOTER_W
        max_dy = new_h - FOOTER_H
        dx = int(max_dx * progress * 0.5)  # 只移動一半
        dy = int(max_dy * 0.3)  # 固定垂直偏移
        
        # 確保不越界
        dx = max(0, min(dx, max_dx))
        dy = max(0, min(dy, max_dy))
        
        # 裁剪到footer尺寸
        frame = resized.crop((dx, dy, dx + FOOTER_W, dy + FOOTER_H))
        # 調整到目標尺寸
        frame = frame.resize((FOOTER_W, FOOTER_H), Image.LANCZOS)
        frames.append(frame)
    
    # 儲存為動畫GIF
    frames[0].save(
        dst_path,
        save_all=True,
        append_images=frames[1:],
        duration=DURATION,
        loop=0,
        optimize=True,
        quality=85
    )
    size_kb = os.path.getsize(dst_path) / 1024
    print(f"  ✅ {name}: {size_kb:.0f}KB, {FRAMES}幀, {DURATION}ms/幀")
    return True

def main():
    print("=== 下載背景圖 ===")
    download_images()
    
    print("\n=== 製作動畫GIF ===")
    success = 0
    for name in THEMES:
        if create_gif(name):
            success += 1
    
    print(f"\n完成: {success}/{len(THEMES)} 個動畫GIF")

if __name__ == "__main__":
    main()
