# -*- coding: utf-8 -*-
"""PetLogic 全站審計：斷圖、斷聯、醫療關鍵字分佈。"""
import os, re, json, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"D:\www\petlogic.org")
os.chdir(ROOT)

# 收集所有 HTML 檔案
html_files = [Path("index.html"), Path("blog.html"), Path("404.html")]
html_files += sorted(Path(".").glob("*.html"))
html_files += sorted(Path("posts").glob("*.html"))
# 去重
html_files = sorted(set(html_files))

# 收集所有實際存在的資源檔（相對 ROOT）
existing_files = set()
for p in ROOT.rglob("*"):
    if p.is_file():
        rel = p.relative_to(ROOT).as_posix()
        existing_files.add(rel)

img_re = re.compile(r'<img[^>]+src=["\']([^"\']+)["\']', re.I)
srcset_re = re.compile(r'<img[^>]+srcset=["\']([^"\']+)["\']', re.I)
a_re   = re.compile(r'<a[^>]+href=["\']([^"\']+)["\']', re.I)
ogimg_re = re.compile(r'(?:og:image|twitter:image)"?\s+content=["\']([^"\']+)["\']', re.I)

broken_imgs = []   # (page, src)
broken_links = []  # (page, href)
missing_og = []    # (page, og_image_url)

# 醫療關鍵字（中英混合）
medical_keywords = [
    "就醫", "獸醫", "獸醫院", "用藥", "服藥", "劑量", "疫苗", "施打", "施打",
    "手術", "開刀", "治療", "診斷", "疾病", "病症", "症狀", "發病",
    "腎病", "腎衰竭", "糖尿病", "癡呆", "認知障礙", "關節炎", "骨關節",
    "心臟病", "癌症", "腫瘤", "癲癇", "麻", "藥物", "抗生素", "消炎",
    "輸液", "打針", "抽血", "檢查報告", "生化", "血常規", "尿常規",
    "安樂", "安寧", "臨終", "臨終關懷", "臨終照護", "臨終階段",
    "驅蟲", "滴藥", "耳藥", "眼藥", "皮膚病", "黴菌", "寄生蟲",
    "發炎", "感染", "病毒", "細菌", "傳染病", "細小", "貓瘟",
    "結紮", "絕育", "不孕", "發情", "懷孕", "流產",
    "營養針", "輸精", "驗孕", "產檢", "生產", "難產",
]

medical_hits = defaultdict(list)  # page -> [kw, ...]

def resolve(page: Path, url: str):
    """把 src/href 轉成本機相對路徑，回傳 None 表示外部 URL 或錨點。"""
    if not url:
        return None
    if url.startswith(("http://", "https://", "//", "mailto:", "tel:", "javascript:", "#")):
        return None
    # 去掉 query/fragment
    u = url.split("#", 1)[0].split("?", 1)[0]
    if not u:
        return None
    # 相對路徑：相對於 page 所在目錄
    base = page.parent
    if u.startswith("/"):
        target = ROOT / u.lstrip("/")
    else:
        target = (base / u).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return None
    return target

for page in html_files:
    if not page.exists():
        continue
    text = page.read_text(encoding="utf-8", errors="replace")

    # 圖片
    for m in img_re.finditer(text):
        src = m.group(1).strip()
        tgt = resolve(page, src)
        if tgt is not None and not tgt.exists():
            broken_imgs.append((page.as_posix(), src))

    # og:image
    for m in ogimg_re.finditer(text):
        u = m.group(1)
        if u.startswith("https://petlogic.org/"):
            rel = u.replace("https://petlogic.org/", "")
            if rel not in existing_files:
                missing_og.append((page.as_posix(), u))

    # 連結
    for m in a_re.finditer(text):
        href = m.group(1).strip()
        tgt = resolve(page, href)
        if tgt is not None and not tgt.exists():
            broken_links.append((page.as_posix(), href))

    # 醫療關鍵字（只掃 body 可見文字，粗略）
    body = text
    for kw in medical_keywords:
        if kw in body:
            # 計算出現次數
            cnt = body.count(kw)
            medical_hits[page.as_posix()].append((kw, cnt))

# 輸出報告
report = {
    "total_html_pages": len(html_files),
    "total_existing_files": len(existing_files),
    "broken_images": broken_imgs,
    "broken_links": broken_links,
    "missing_og_images": missing_og,
    "medical_hits": {k: v for k, v in sorted(medical_hits.items())},
}

out = ROOT / "_audit_report.json"
out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

# 文字摘要
print(f"=== 全站審計摘要 ===")
print(f"HTML 頁數: {len(html_files)}")
print(f"實際檔案數: {len(existing_files)}")
print(f"斷圖數: {len(broken_imgs)}")
print(f"斷聯數: {len(broken_links)}")
print(f"OG 圖缺失: {len(missing_og)}")
print(f"含醫療關鍵字頁數: {len(medical_hits)}")
print()
print("--- 斷圖（前 30）---")
for p, s in broken_imgs[:30]:
    print(f"  {p}  ->  {s}")
print()
print("--- 斷聯（前 30）---")
for p, h in broken_links[:30]:
    print(f"  {p}  ->  {h}")
print()
print("--- OG 圖缺失 ---")
for p, u in missing_og:
    print(f"  {p}  ->  {u}")
print()
print("--- 醫療關鍵字分佈（頁數：關鍵字）---")
for page, hits in sorted(medical_hits.items()):
    kws = ", ".join(f"{k}×{c}" for k, c in sorted(hits, key=lambda x: -x[1]))
    print(f"  {page}: {kws}")
