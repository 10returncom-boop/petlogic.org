#!/usr/bin/env python3
"""
PetLogic 佔位圖片產生器
產生網站所需的 WebP 佔位圖片（分類色 + 文字標示）。
實際部署時請替換為真實圖片。
"""
import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = os.path.join(BASE_DIR, "images")

# 分類對應顏色（R, G, B）
CATEGORY_COLORS = {
    "cat": (42, 157, 143),        # teal
    "dog": (231, 111, 81),        # coral
    "health": (38, 70, 83),       # dark teal
    "training": (244, 162, 97),   # orange
    "nutrition": (233, 196, 106), # yellow
    "exotic": (138, 177, 125),    # green
    "care": (154, 140, 152),      # purple-gray
    "lifestyle": (72, 128, 152),  # blue
}

CATEGORY_ICONS = {
    "cat": "🐱",
    "dog": "🐶",
    "health": "🏥",
    "training": "🧠",
    "nutrition": "🍖",
    "exotic": "🦎",
    "care": "✂️",
    "lifestyle": "🏡",
}


def get_font(size):
    """嘗試取得中文字型"""
    font_paths = [
        "C:/Windows/Fonts/msjh.ttc",      # 微軟正黑體
        "C:/Windows/Fonts/msyh.ttc",      # 微軟雅黑
        "C:/Windows/Fonts/simhei.ttf",    # 黑體
        "/System/Library/Fonts/PingFang.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    ]
    for path in font_paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def create_placeholder(filename, category, width=1200, height=800, label=""):
    """產生單張佔位圖"""
    color = CATEGORY_COLORS.get(category, (100, 100, 100))
    icon = CATEGORY_ICONS.get(category, "🐾")

    # 建立漸層背景
    img = Image.new("RGB", (width, height), color)
    draw = ImageDraw.Draw(img)

    # 簡單漸層效果（從上到下變亮）
    for y in range(height):
        ratio = y / height
        r = int(color[0] + (255 - color[0]) * ratio * 0.3)
        g = int(color[1] + (255 - color[1]) * ratio * 0.3)
        b = int(color[2] + (255 - color[2]) * ratio * 0.3)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # 畫圓形裝飾
    draw.ellipse([width*0.7, -height*0.2, width*1.2, height*0.4],
                 fill=(color[0]+30, color[1]+30, color[2]+30))
    draw.ellipse([-width*0.15, height*0.6, width*0.25, height*1.1],
                 fill=(color[0]-20, color[1]-20, color[2]-20))

    # 中央 icon + 文字
    try:
        icon_font = get_font(int(width * 0.12))
        text_font = get_font(int(width * 0.04))
        label_font = get_font(int(width * 0.025))

        # 計算文字位置
        icon_bbox = draw.textbbox((0, 0), icon, font=icon_font)
        icon_w = icon_bbox[2] - icon_bbox[0]
        icon_h = icon_bbox[3] - icon_bbox[1]
        draw.text(((width - icon_w) // 2, height * 0.3), icon, font=icon_font, fill=(255, 255, 255))

        title = "PetLogic"
        title_bbox = draw.textbbox((0, 0), title, font=text_font)
        title_w = title_bbox[2] - title_bbox[0]
        draw.text(((width - title_w) // 2, height * 0.55), title, font=text_font, fill=(255, 255, 255))

        if label:
            label_bbox = draw.textbbox((0, 0), label, font=label_font)
            label_w = label_bbox[2] - label_bbox[0]
            draw.text(((width - label_w) // 2, height * 0.68), label, font=label_font, fill=(255, 255, 255, 200))
    except Exception:
        pass

    filepath = os.path.join(IMAGES_DIR, filename)
    img.save(filepath, "WEBP", quality=80)
    print(f"  ✓ {filename} ({width}x{height})")


def create_simple_image(filename, color, width, height, text=""):
    """產生簡單纯色圖片（用於 logo、favicon 等）"""
    img = Image.new("RGBA", (width, height), color + (255,))
    draw = ImageDraw.Draw(img)
    if text:
        try:
            font = get_font(int(width * 0.4))
            bbox = draw.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]
            draw.text(((width - tw) // 2, (height - th) // 2 - bbox[1]),
                      text, font=font, fill=(255, 255, 255, 255))
        except Exception:
            pass
    filepath = os.path.join(IMAGES_DIR, filename)
    if filename.endswith(".webp"):
        img.convert("RGB").save(filepath, "WEBP", quality=90)
    else:
        img.save(filepath)
    print(f"  ✓ {filename} ({width}x{height})")


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    print("產生 PetLogic 佔位圖片...")

    # Logo 和 OG 圖片
    create_simple_image("logo.webp", (42, 157, 143), 512, 512, "🐾")
    create_simple_image("favicon.png", (42, 157, 143), 64, 64, "🐾")
    create_simple_image("apple-touch-icon.png", (42, 157, 143), 180, 180, "🐾")
    create_placeholder("og-image.webp", "cat", 1200, 630, "寵物知識百科")
    create_placeholder("banner.webp", "cat", 1920, 600, "用科學邏輯理解毛孩")
    create_placeholder("social-logo.webp", "cat", 1200, 630, "PetLogic")

    # 各分類文章配圖（每個分類 4 張）
    categories = ["cat", "dog", "health", "training", "nutrition", "exotic", "care", "lifestyle"]
    labels = {
        "cat": "貓咪百科",
        "dog": "狗狗百科",
        "health": "寵物健康",
        "training": "行為訓練",
        "nutrition": "寵物營養",
        "exotic": "異寵世界",
        "care": "日常照護",
        "lifestyle": "人寵生活",
    }

    for cat in categories:
        for i in range(1, 5):
            suffix = "" if i == 1 else str(i)
            create_placeholder(
                f"placeholder-{cat}{suffix}.webp",
                cat, 1200, 800,
                labels[cat]
            )

    print(f"\n完成！所有圖片已儲存到 {IMAGES_DIR}")
    print("注意：這些是佔位圖片，部署前請替換為真實圖片。")


if __name__ == "__main__":
    main()
