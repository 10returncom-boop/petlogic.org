#!/usr/bin/env python3
"""下載90張文章專屬圖片並更新文章資料"""
import os
import urllib.request
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(BASE_DIR, "images")

# 90篇文章的專屬圖片URL映射
IMAGE_MAP = {
    # 貓行為實驗室
    "post-012": "https://aka.doubaocdn.com/s/4gxfS276E5",
    "post-013": "https://aka.doubaocdn.com/s/dmHh9eu23U",
    "post-014": "https://aka.doubaocdn.com/s/MU0U8s5Zjx",
    "post-015": "https://aka.doubaocdn.com/s/0Vx32lDQEL",
    "post-016": "https://aka.doubaocdn.com/s/XuLsCHK7iU",
    "post-017": "https://aka.doubaocdn.com/s/3i96jMqAKr",
    "post-018": "https://aka.doubaocdn.com/s/oU9X80oud5",
    "post-019": "https://aka.doubaocdn.com/s/K2hG84Qupv",
    "post-020": "https://aka.doubaocdn.com/s/vgggEyVuNe",
    # 狗訓練科學
    "post-021": "https://aka.doubaocdn.com/s/wWQv2RSb7D",
    "post-022": "https://aka.doubaocdn.com/s/pilXcF3OUq",
    "post-023": "https://aka.doubaocdn.com/s/b4HNf6Bhh2",
    "post-024": "https://aka.doubaocdn.com/s/J7nmTvYDKc",
    "post-025": "https://aka.doubaocdn.com/s/xNDWo5sUn1",
    "post-026": "https://aka.doubaocdn.com/s/59QBTBKXFw",
    "post-027": "https://aka.doubaocdn.com/s/JMXAU8W1F4",
    "post-028": "https://aka.doubaocdn.com/s/4QvxwlQob0",
    "post-029": "https://aka.doubaocdn.com/s/93UVB2lfmH",
    # 寵物營養實驗室
    "post-030": "https://aka.doubaocdn.com/s/v2oqugQpXb",
    "post-031": "https://aka.doubaocdn.com/s/IQr1kKARF6",
    "post-032": "https://aka.doubaocdn.com/s/doPW2mJAuH",
    "post-033": "https://aka.doubaocdn.com/s/pUaN4r4kSa",
    "post-034": "https://aka.doubaocdn.com/s/iwC6rj991G",
    "post-035": "https://aka.doubaocdn.com/s/4ZZGgpj07n",
    "post-036": "https://aka.doubaocdn.com/s/UvpdBZ0YeS",
    "post-037": "https://aka.doubaocdn.com/s/KcIY6Oojzo",
    "post-038": "https://aka.doubaocdn.com/s/MKZGhvPb2i",
    # 高齡寵物學
    "post-039": "https://aka.doubaocdn.com/s/OkJaZbtLJB",
    "post-040": "https://aka.doubaocdn.com/s/T9F9VqZHjs",
    "post-041": "https://aka.doubaocdn.com/s/8V3LHYbnIf",
    "post-042": "https://aka.doubaocdn.com/s/0VzAfP4TOT",
    "post-043": "https://aka.doubaocdn.com/s/NmjIJY0a4y",
    "post-044": "https://aka.doubaocdn.com/s/IkXZMYsrFN",
    "post-045": "https://aka.doubaocdn.com/s/wvI6Vi3umK",
    "post-046": "https://aka.doubaocdn.com/s/UkpvUPV4vw",
    "post-047": "https://aka.doubaocdn.com/s/X65PlqrVfV",
    # 幼犬幼貓成長誌
    "post-048": "https://aka.doubaocdn.com/s/12tMlqgGdj",
    "post-049": "https://aka.doubaocdn.com/s/YclpjXvblS",
    "post-050": "https://aka.doubaocdn.com/s/CsafBHpi6l",
    "post-051": "https://aka.doubaocdn.com/s/GjoHnZiymM",
    "post-052": "https://aka.doubaocdn.com/s/Ht7YNVyvUv",
    "post-053": "https://aka.doubaocdn.com/s/CaqdqPffV5",
    "post-054": "https://aka.doubaocdn.com/s/F80cfyrJuc",
    "post-055": "https://aka.doubaocdn.com/s/6YzgTmZuXg",
    "post-056": "https://aka.doubaocdn.com/s/6orgIJDUdP",
    # 異寵物種誌
    "post-057": "https://aka.doubaocdn.com/s/0q9neKaVhu",
    "post-058": "https://aka.doubaocdn.com/s/sK4fzwBMy6",
    "post-059": "https://aka.doubaocdn.com/s/D8nT2grzaQ",
    "post-060": "https://aka.doubaocdn.com/s/dZcdU2rkcV",
    "post-061": "https://aka.doubaocdn.com/s/hUpgIrg78m",
    "post-062": "https://aka.doubaocdn.com/s/Jga48qMHKH",
    "post-063": "https://aka.doubaocdn.com/s/a19bVJXXN5",
    "post-064": "https://aka.doubaocdn.com/s/wd1R6PKggR",
    "post-065": "https://aka.doubaocdn.com/s/BBcY4Zx6B7",
    # 寵物與城市
    "post-066": "https://aka.doubaocdn.com/s/I95VTo1Yq8",
    "post-067": "https://aka.doubaocdn.com/s/y8a6YNQnVb",
    "post-068": "https://aka.doubaocdn.com/s/kfcBDeOHao",
    "post-069": "https://aka.doubaocdn.com/s/3QCwAOugAk",
    "post-070": "https://aka.doubaocdn.com/s/TnrsUT2EzS",
    "post-071": "https://aka.doubaocdn.com/s/XuS121POW7",
    "post-072": "https://aka.doubaocdn.com/s/0kcfUuX60F",
    "post-073": "https://aka.doubaocdn.com/s/5gc08dj7Oz",
    "post-074": "https://aka.doubaocdn.com/s/sshb2zQUaa",
    # 寵物文化誌
    "post-075": "https://aka.doubaocdn.com/s/v74ffyEcG6",
    "post-076": "https://aka.doubaocdn.com/s/tq03bdRY1I",
    "post-077": "https://aka.doubaocdn.com/s/zGuz9ltKbX",
    "post-078": "https://aka.doubaocdn.com/s/dBCFUEA3kf",
    "post-079": "https://aka.doubaocdn.com/s/H5w8jdsdBd",
    "post-080": "https://aka.doubaocdn.com/s/VRIw4DlTFU",
    "post-081": "https://aka.doubaocdn.com/s/Qlw6nu65XC",
    "post-082": "https://aka.doubaocdn.com/s/NnM2MdJ3fo",
    "post-083": "https://aka.doubaocdn.com/s/ea522cb1iL",
    # 寵物商品科學
    "post-084": "https://aka.doubaocdn.com/s/LVFR3WB8KA",
    "post-085": "https://aka.doubaocdn.com/s/ekaafuw3Ia",
    "post-086": "https://aka.doubaocdn.com/s/ZLSKcy6Wrk",
    "post-087": "https://aka.doubaocdn.com/s/aaHa2tQ3OE",
    "post-088": "https://aka.doubaocdn.com/s/flkm2bMn3Z",
    "post-089": "https://aka.doubaocdn.com/s/wisdoUrDye",
    "post-090": "https://aka.doubaocdn.com/s/skOsfEMUo0",
    "post-091": "https://aka.doubaocdn.com/s/wESfxnxb6T",
    "post-092": "https://aka.doubaocdn.com/s/rqYXoUVUHj",  # 用寵物攝影機圖
    # 順寵好物推薦
    "post-093": "https://aka.doubaocdn.com/s/5wja8ux14P",
    "post-094": "https://aka.doubaocdn.com/s/i4mj2zBRjM",
    "post-095": "https://aka.doubaocdn.com/s/Km01rJ5TH2",
    "post-096": "https://aka.doubaocdn.com/s/rqYXoUVUHj",
    "post-097": "https://aka.doubaocdn.com/s/XCpuBnKW7y",
    "post-098": "https://aka.doubaocdn.com/s/01UqHN6EiY",
    "post-099": "https://aka.doubaocdn.com/s/w9TA8eS5V0",
    "post-100": "https://aka.doubaocdn.com/s/zstnFflPVH",
    "post-101": "https://aka.doubaocdn.com/s/nKAv22oH8a",
}

def download_images():
    """下載所有圖片"""
    os.makedirs(IMG_DIR, exist_ok=True)
    success = 0
    failed = []
    for aid, url in IMAGE_MAP.items():
        filename = f"hero-{aid}.webp"
        filepath = os.path.join(IMG_DIR, filename)
        if os.path.exists(filepath) and os.path.getsize(filepath) > 10000:
            success += 1
            continue
        try:
            urllib.request.urlretrieve(url, filepath)
            if os.path.getsize(filepath) > 10000:
                success += 1
            else:
                failed.append(aid)
        except Exception as e:
            failed.append(f"{aid}: {e}")
    print(f"Downloaded: {success}/{len(IMAGE_MAP)}")
    if failed:
        print(f"Failed: {failed}")
    return success, failed

def update_article_data():
    """更新文章資料檔案的圖片引用"""
    from articles_data import ARTICLES_90 as A1
    from articles_data_2 import ARTICLES_63 as A2
    from articles_data_3 import ARTICLES_36 as A3
    
    all_articles = A1 + A2 + A3
    updated = 0
    for art in all_articles:
        aid = art["id"]
        if aid in IMAGE_MAP:
            hero_img = f"hero-{aid}.webp"
            art["img1"] = hero_img
            # 第二張圖用現有相關圖
            art["img2"] = hero_img  # 先用同一張，後續可優化
            updated += 1
    print(f"Updated {updated} articles with unique hero images")
    return all_articles

if __name__ == "__main__":
    print("=== 下載圖片 ===")
    download_images()
    print("\n=== 更新文章資料 ===")
    update_article_data()
    print("\n完成！")
