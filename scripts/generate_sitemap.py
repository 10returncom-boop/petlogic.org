#!/usr/bin/env python3
"""
PetLogic Sitemap 產生器
自動掃描網站目錄中的 HTML 檔案，產生符合標準的 sitemap.xml。

用法: python generate_sitemap.py
"""
import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_URL = "https://petlogic.org"

# 頁面優先級設定
PRIORITY_MAP = {
    "index.html": "1.0",
    "blog.html": "0.9",
}

# 變更頻率
CHANGEFREQ_MAP = {
    "index.html": "daily",
    "blog.html": "daily",
}

# 分類頁
CATEGORY_PAGES = [
    "cat-encyclopedia.html",
    "dog-encyclopedia.html",
    "pet-health.html",
    "pet-behavior.html",
    "exotic-pets.html",
    "pet-nutrition.html",
    "pet-care.html",
    "pet-lifestyle.html",
]


def get_file_mod_date(filepath):
    """取得檔案最後修改日期"""
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
    except OSError:
        return datetime.date.today().strftime("%Y-%m-%d")


def generate_sitemap():
    urls = []

    # 根目錄 HTML
    for fname in sorted(os.listdir(BASE_DIR)):
        if fname.endswith(".html") and fname != "404.html":
            filepath = os.path.join(BASE_DIR, fname)
            priority = PRIORITY_MAP.get(fname, "0.8")
            changefreq = CHANGEFREQ_MAP.get(fname, "weekly")
            if fname in CATEGORY_PAGES:
                priority = "0.8"
                changefreq = "weekly"
            urls.append({
                "loc": f"{SITE_URL}/{fname}",
                "lastmod": get_file_mod_date(filepath),
                "changefreq": changefreq,
                "priority": priority,
            })

    # posts 目錄中的文章
    posts_dir = os.path.join(BASE_DIR, "posts")
    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir)):
            if fname.endswith(".html"):
                filepath = os.path.join(posts_dir, fname)
                urls.append({
                    "loc": f"{SITE_URL}/posts/{fname}",
                    "lastmod": get_file_mod_date(filepath),
                    "changefreq": "monthly",
                    "priority": "0.6",
                })

    # 產生 XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
    xml += '        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'

    for u in urls:
        xml += "  <url>\n"
        xml += f'    <loc>{u["loc"]}</loc>\n'
        xml += f'    <lastmod>{u["lastmod"]}</lastmod>\n'
        xml += f'    <changefreq>{u["changefreq"]}</changefreq>\n'
        xml += f'    <priority>{u["priority"]}</priority>\n'
        xml += "  </url>\n"

    xml += "</urlset>\n"

    output_path = os.path.join(BASE_DIR, "sitemap.xml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(xml)

    print(f"  ✓ sitemap.xml 已產生，共 {len(urls)} 個 URL")
    return len(urls)


def generate_rss():
    """產生 RSS 2.0 feed"""
    posts = []
    posts_dir = os.path.join(BASE_DIR, "posts")
    if os.path.isdir(posts_dir):
        for fname in sorted(os.listdir(posts_dir), reverse=True):
            if fname.endswith(".html"):
                filepath = os.path.join(posts_dir, fname)
                # 從檔案中提取標題和描述
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    title = ""
                    desc = ""
                    for line in content.split("\n"):
                        if '<title>' in line and not title:
                            title = line.split("<title>")[1].split("</title>")[0].split(" | ")[0]
                        if 'name="description"' in line and not desc:
                            desc = line.split('content="')[1].split('"')[0]
                    if not title:
                        title = fname
                    posts.append({
                        "title": title,
                        "link": f"{SITE_URL}/posts/{fname}",
                        "desc": desc,
                        "date": get_file_mod_date(filepath),
                    })
                except Exception:
                    pass

    now = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0800")

    rss = '<?xml version="1.0" encoding="UTF-8"?>\n'
    rss += '<rss version="2.0">\n'
    rss += "  <channel>\n"
    rss += f"    <title>PetLogic 寵物知識百科</title>\n"
    rss += f"    <link>{SITE_URL}</link>\n"
    rss += f"    <description>用科學邏輯理解毛孩，讓每一位飼主都能安心養寵。涵蓋貓狗飼養、行為解析、健康護理、品種圖鑑與異寵照護。</description>\n"
    rss += f"    <language>zh-TW</language>\n"
    rss += f"    <lastBuildDate>{now}</lastBuildDate>\n"
    rss += f'    <image><url>{SITE_URL}/images/logo.webp</url><title>PetLogic</title><link>{SITE_URL}</link></image>\n'

    for p in posts[:20]:  # 最新20篇
        rss += "    <item>\n"
        rss += f"      <title>{p['title']}</title>\n"
        rss += f"      <link>{p['link']}</link>\n"
        rss += f"      <description>{p['desc']}</description>\n"
        rss += f"      <pubDate>{p['date']}</pubDate>\n"
        rss += f"      <guid>{p['link']}</guid>\n"
        rss += "    </item>\n"

    rss += "  </channel>\n"
    rss += "</rss>\n"

    output_path = os.path.join(BASE_DIR, "rss.xml")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rss)

    print(f"  ✓ rss.xml 已產生，共 {len(posts[:20])} 篇文章")


if __name__ == "__main__":
    print("產生 PetLogic 網站地圖與 RSS...")
    count = generate_sitemap()
    generate_rss()
    print(f"\n完成！sitemap 包含 {count} 個 URL")
