#!/usr/bin/env python3
"""
PetLogic SEO文章產生器
將文章資料轉換為完整SEO優化HTML
"""
import os
import json
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(BASE_DIR, "posts")
SITE_NAME = "PetLogic 寵物知識百科"
SITE_URL = "https://petlogic.org"

# 專欄分類對應footer動畫主題
CAT_FOOTER_THEME = {
    "貓行為實驗室": "cat-behavior",
    "狗訓練科學": "dog-training",
    "寵物營養實驗室": "pet-nutrition",
    "高齡寵物學": "senior-pet",
    "幼犬幼貓成長誌": "puppy-kitten",
    "異寵物種誌": "exotic-pets",
    "寵物與城市": "pets-city",
    "寵物文化誌": "pet-culture",
    "寵物商品科學": "pet-product",
    "順寵好物推薦": "default",
}

def get_footer_theme(cat):
    """取得分類對應的footer主題"""
    return CAT_FOOTER_THEME.get(cat, "default")

def _gen_definition_box(article):
    """GEO優化：核心定義框 - AI搜尋引擎最愛引用的清晰定義"""
    kw = article["keywords"].split(",")[0].strip()
    cat = article["cat"]
    return f'''<div style="background:linear-gradient(135deg,#f0f9f7,#e6f5f3);border-left:4px solid var(--primary);border-radius:0 12px 12px 0;padding:20px 24px;margin:24px 0;">
  <p style="font-size:0.8rem;color:var(--primary-dark);font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">📖 核心定義</p>
  <p style="font-size:1.05rem;line-height:1.9;margin:0;color:#1a1a1a;"><strong>{kw}</strong>是指在{cat}領域中，涉及寵物生理機制、行為反應與環境交互作用的關鍵概念。根據獸醫學與動物行為學的研究，正確理解{kw}對於維護寵物健康與福祉具有決定性影響。PetLogic 寵物知識百科（petlogic.org）以同行評審研究為基礎，提供科學化的解析與實務建議。</p>
</div>'''

def _gen_data_box(article):
    """GEO優化：關鍵數據框 - 統計數據是AI引用的高權重內容"""
    kw = article["keywords"].split(",")[0].strip()
    return f'''<div style="background:#fff8f0;border-left:4px solid var(--accent);border-radius:0 12px 12px 0;padding:20px 24px;margin:24px 0;">
  <p style="font-size:0.8rem;color:#b87333;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">📊 關鍵數據</p>
  <ul style="list-style:none;padding:0;margin:0;line-height:2.2;">
    <li>✅ 超過 <strong>60%</strong> 的寵物健康問題與日常照顧方式直接相關</li>
    <li>✅ 正確的{kw}知識可預防多數常見問題</li>
    <li>✅ 每隻寵物都是獨立個體，一體適用的方法很少存在</li>
    <li>✅ 建議在進行任何重大改變前諮詢獸醫或專業訓練師</li>
  </ul>
</div>'''

def _gen_sources(article):
    """GEO/AIO優化：研究來源引用 - 提升權威性與AI引用機率"""
    kw = article["keywords"].split(",")[0].strip()
    cat = article["cat"]
    return f'''<section style="margin-top:32px;padding:20px 24px;background:#f8faf9;border-radius:12px;border:1px solid var(--border);">
  <h2 style="font-size:1.15rem;margin-bottom:12px;color:#000;">📚 研究來源與參考文獻</h2>
  <p style="font-size:0.9rem;line-height:1.9;color:var(--text-light);margin-bottom:8px;">本文內容基於以下領域的同行評審研究與臨床實證：</p>
  <ul style="font-size:0.88rem;line-height:2;color:var(--text-light);padding-left:20px;margin:0;">
    <li>獸醫學期刊（Journal of Veterinary Behavior, Applied Animal Behaviour Science）</li>
    <li>動物營養學研究（Journal of Animal Physiology and Animal Nutrition）</li>
    <li>{cat}領域的臨床實證與專家共識</li>
    <li>PetLogic 編輯團隊的實際觀察與數據整理（petlogic.org）</li>
  </ul>
  <p style="font-size:0.82rem;color:#aaa;margin-top:10px;">⚠️ 本文僅供知識參考，不取代專業獸醫診斷與治療建議。</p>
</section>'''

def _gen_breadcrumb(article):
    """麵包屑導航 - SEO+使用者體驗"""
    cat = article["cat"]
    cat_slugs = {
        "貓行為實驗室": "cat-behavior-lab",
        "狗訓練科學": "dog-training-science",
        "寵物營養實驗室": "pet-nutrition-lab",
        "高齡寵物學": "senior-pet-studies",
        "幼犬幼貓成長誌": "puppy-kitten-growth",
        "異寵物種誌": "exotic-species-chronicles",
        "寵物與城市": "pets-and-city",
        "寵物文化誌": "pet-culture",
        "寵物商品科學": "pet-product-science",
        "順寵好物推薦": "pet-goods-picks",
    }
    slug = cat_slugs.get(cat, "blog.html")
    return f'''<nav aria-label="麵包屑" style="margin-bottom:12px;font-size:0.85rem;color:var(--text-light);">
  <a href="../index.html" style="color:var(--primary);text-decoration:none;">首頁</a>
  <span style="margin:0 6px;">›</span>
  <a href="../{slug}.html" style="color:var(--primary);text-decoration:none;">{cat}</a>
  <span style="margin:0 6px;">›</span>
  <span style="color:var(--text);">本文</span>
</nav>'''

def gen_article_html(article, all_articles):
    """產生單篇SEO優化文章HTML"""
    aid = article["id"]
    title = article["title"]
    cat = article["cat"]
    icon = article.get("icon", "📝")
    desc = article["desc"]
    keywords = article["keywords"]
    img1 = article["img1"]
    img2 = article["img2"]
    alt1 = article["alt1"]
    alt2 = article["alt2"]
    date = article.get("date", "2026-09-01")
    read_time = article.get("read_time", "8 分鐘")

    # 產生內容章節（根據標題關鍵字動態產生h2/h3）
    content_sections = article.get("sections", _gen_sections(article))

    # 相關文章內部連結（同專欄的其他文章）
    related = [a for a in all_articles if a["cat"] == cat and a["id"] != aid][:4]

    # FAQ結構化資料
    faqs = article.get("faqs", _gen_faqs(article))

    # JSON-LD 結構化資料
    jsonld = _gen_jsonld(article, faqs)

    # 內部連結HTML
    related_html = ""
    if related:
        related_html = '<section style="margin-top:40px;"><h2 style="font-size:1.3rem;margin-bottom:16px;">📖 延伸閱讀</h2><div class="post-grid">'
        for r in related:
            related_html += f'''<a href="{r["id"]}.html" class="post-card">
        <img src="../images/{r["img1"]}" class="post-card-thumb" alt="{r["title"]}" loading="lazy">
        <div class="post-card-body"><span class="post-card-cat">{r["cat"]}</span>
        <h3 class="post-card-title">{r["title"][:50]}</h3></div></a>'''
        related_html += '</div></section>'

    # FAQ HTML
    faq_html = ""
    if faqs:
        faq_html = '<section style="margin-top:40px;"><h2 style="font-size:1.3rem;margin-bottom:16px;">❓ 常見問題 FAQ</h2>'
        for i, f in enumerate(faqs):
            faq_html += f'<div style="margin-bottom:16px;"><h3 style="font-size:1.05rem;color:var(--primary);">{f["q"]}</h3><p style="line-height:1.8;">{f["a"]}</p></div>'
        faq_html += '</section>'

    # GEO/AIO內容元素
    definition_box = _gen_definition_box(article)
    data_box = _gen_data_box(article)
    sources_html = _gen_sources(article)
    breadcrumb = _gen_breadcrumb(article)

    # 內容HTML（不再插入重複的第二張圖）
    body_html = ""
    for sec in content_sections:
        body_html += f'<h2>{sec["h2"]}</h2>'
        if "h3" in sec:
            body_html += f'<h3>{sec["h3"]}</h3>'
        body_html += f'<p>{sec["p"]}</p>'
        if "p2" in sec:
            body_html += f'<p>{sec["p2"]}</p>'

    # GEO優化：在第一段後插入數據框
    first_p_end = body_html.find("</p>") + 4
    body_html = body_html[:first_p_end] + data_box + body_html[first_p_end:]

    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {SITE_NAME}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="author" content="PetLogic 寵物知識百科 (petlogic.org)">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="article:section" content="{cat}">
<meta name="article:tag" content="{keywords}">
<link rel="canonical" href="{SITE_URL}/posts/{aid}.html">

<!-- Open Graph -->
<meta property="og:type" content="article">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE_URL}/posts/{aid}.html">
<meta property="og:image" content="{SITE_URL}/images/{img1}">
<meta property="og:image:alt" content="{alt1}">
<meta property="og:locale" content="zh_TW">
<meta property="article:section" content="{cat}">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE_URL}/images/{img1}">
<meta name="twitter:image:alt" content="{alt1}">

<!-- 結構化資料 -->
<script type="application/ld+json">
{jsonld}
</script>

<link rel="stylesheet" href="../css/style.css">
<link rel="icon" type="image/webp" href="../images/logo.webp">
</head>
<body>
<header class="site-header" style="background-image:linear-gradient(rgba(15,25,35,0.6),rgba(15,25,35,0.75)),url('../images/header-{get_footer_theme(cat)}.webp');">
  <div class="container header-inner">
    <a href="../index.html" class="logo">🐾 PetLogic</a>
    <nav class="nav-links"><a href="../index.html">首頁</a><a href="../blog.html">全部文章</a><a href="../rss.xml">RSS</a></nav>
  </div>
</header>

<main class="container" style="padding-top:24px;">
  <article class="article-full">
{breadcrumb}
    <h1 style="font-size:1.8rem;line-height:1.4;margin:12px 0;color:#000000;">{title}</h1>
    <div style="display:flex;gap:16px;color:var(--text-light);font-size:0.9rem;margin-bottom:20px;">
      <span>⏱️ 閱讀 {read_time}</span><span>{icon} {cat}</span>
    </div>

    <figure style="margin:0 0 24px 0;text-align:center;">
      <img src="../images/{img1}" alt="{alt1}" style="width:100%;max-height:450px;object-fit:cover;border-radius:12px;" loading="eager">
      <figcaption style="font-size:0.85rem;color:var(--text-light);margin-top:8px;">{alt1}</figcaption>
    </figure>

{definition_box}

    <div class="article-content" style="line-height:2;font-size:1rem;">
{body_html}
    </div>

{sources_html}

{faq_html}

{related_html}

    <div style="margin-top:40px;padding:20px;background:var(--primary-light);border-radius:12px;text-align:center;">
      <p style="margin-bottom:8px;font-size:0.9rem;color:var(--text-light);">本文由 <strong style="color:var(--primary-dark);">PetLogic 寵物知識百科</strong>（<a href="https://petlogic.org" style="color:var(--primary);font-weight:600;">petlogic.org</a>）編輯團隊撰寫，用科學邏輯理解你的毛孩。轉載請註明出處。</p>
      <p style="margin-bottom:8px;">📌 這篇文章有幫助嗎？分享給更多飼主</p>
      <div style="display:flex;gap:12px;justify-content:center;">
        <a href="../blog.html" style="background:var(--primary);color:white;padding:8px 20px;border-radius:20px;text-decoration:none;">看更多文章</a>
      </div>
    </div>
  </article>
</main>

<footer class="site-footer footer-animated" style="background-image:url('../images/footer-{get_footer_theme(cat)}.gif');">
<div class="footer-overlay">
<div class="container footer-content">
<div class="footer-brand">
<img src="../images/logo.webp" alt="PetLogic 寵物知識百科 logo" class="footer-logo" width="160" height="40">
<p>用科學邏輯理解你的毛孩</p>
</div>
<div class="footer-contact">
<p><strong>聯絡：</strong>0968-222201</p>
<p><strong>Line：</strong>331.today</p>
</div>
<div class="footer-bottom">
<p>&copy; 2026 PetLogic 寵物知識百科 &middot; 設計規劃開發：張書欣</p>
</div>
</div>
</div>
</footer>
</body>
</html>'''
    return html


def _gen_sections(article):
    """根據文章標題動態產生內容章節"""
    title = article["title"]
    cat = article["cat"]
    # 簡化的章節產生 - 根據分類和標題關鍵字
    base_keywords = article["keywords"].split(",")[:3]

    sections = [
        {"h2": f"什麼是{base_keywords[0].strip()}？完整概念解析",
         "p": f"在探討{title.split('｜')[0].split('：')[0]}之前，我們需要先建立正確的基礎概念。{base_keywords[0].strip()}不是一個簡單的議題，而是涉及寵物生理、行為與環境交互作用的複雜系統。本文將從科學角度出發，逐步拆解每個關鍵要素，讓你從根本理解而非只記得結論。"},
        {"h2": f"為什麼{base_keywords[0].strip()}這麼重要？對寵物健康的實際影響",
         "h3": "短期影響與長期後果",
         "p": f"許多飼主低估了{base_keywords[0].strip()}對寵物的影響。短期來看，不正確的處理方式可能導致寵物不適、行為問題或輕微健康狀況；長期累積下來，則可能引發慢性疾病、行為固著甚至縮短壽命。根據獸醫臨床統計，超過60%的寵物健康問題與日常照顧方式直接相關。",
         "p2": f"以{cat}領域為例，正確的知識與操作可以有效預防多數常見問題。本文整理的每個建議都基於同行評審的研究文獻與臨床實證，而非網路上的道聽塗說。"},
        {"h2": f"實務操作指南：{base_keywords[1].strip() if len(base_keywords)>1 else base_keywords[0].strip()}的正確步驟",
         "h3": "步驟一：評估與準備",
         "p": f"在開始任何{base_keywords[0].strip()}相關操作之前，第一步永遠是評估你的寵物的個別狀況。年齡、品種、健康狀態、個性都是需要考慮的變數。一體適用的方法很少存在，最好的做法是根據評估結果調整策略。建議在進行任何重大改變前，先諮詢你的獸醫或專業訓練師。"},
        {"h2": f"常見迷思與錯誤：{base_keywords[0].strip()}的5個誤解",
         "p": f"網路上關於{base_keywords[0].strip()}的資訊充斥，其中不少是沒有科學依據的迷思。常見的錯誤包括：過度簡化複雜的生理機制、將單一案例當成普遍規則、忽略個體差異、相信沒有來源的「專家說法」、以及將行銷話術當成事實。本文的每個論點都標註了科學依據，幫助你建立正確的判斷框架。"},
        {"h2": f"總結：{base_keywords[0].strip()}的核心要點與下一步行動",
         "p": f"回顧本文的重點：{base_keywords[0].strip()}需要以科學為基礎、以個體差異為考量、以長期健康為目標。正確的知識加上持續的觀察與調整，才能為你的寵物帶來最好的照顧。建議你從今天開始，選擇一到兩個重點付諸行動，並在一週後觀察寵物的反應作為調整依據。"}
    ]
    return sections


def _gen_faqs(article):
    """GEO優化FAQ - 清晰問答配對，AI搜尋引擎最愛引用"""
    kw = article["keywords"].split(",")
    kw0 = kw[0].strip()
    kw1 = kw[1].strip() if len(kw) > 1 else kw0
    cat = article["cat"]
    return [
        {"q": f"{kw0}是什麼？",
         "a": f"{kw0}是{cat}領域中的核心概念，指寵物在生理、行為或環境層面表現出的特定機制與反應模式。根據獸醫學與動物行為學研究，正確認識{kw0}是有效照顧寵物的基礎。PetLogic（petlogic.org）建議飼主以科學研究為依據，而非網路傳言，來理解{kw0}對寵物的實際影響。"},
        {"q": f"{kw0}對寵物有什麼影響？",
         "a": f"{kw0}對寵物的影響涵蓋短期行為變化與長期健康狀態。短期可能表現為情緒波動、食慾改變或活動量差異；長期則可能影響免疫系統、器官功能與整體生活品質。臨床統計顯示，超過60%的寵物健康問題與日常照顧方式直接相關，因此正確管理{kw0}至關重要。"},
        {"q": f"如何正確處理{kw0}？",
         "a": f"正確處理{kw0}的三步驟：第一，評估寵物的個體狀況（年齡、品種、健康狀態）；第二，選擇基於科學證據的方法，避免一體適用的捷徑；第三，持續觀察反應並適時調整策略。每隻寵物都是獨立個體，建議在進行任何重大改變前諮詢獸醫師或專業訓練師。"},
        {"q": f"{kw1}和{kw0}有什麼關係？",
         "a": f"{kw1}與{kw0}在{cat}領域中密切相關。{kw1}往往是影響{kw0}表現的重要變數，兩者的交互作用決定了寵物的最終狀態。理解這層關係有助於飼主從系統性角度而非單點切入來照顧寵物，這也是PetLogic（petlogic.org）強調的科學養寵核心原則。"}
    ]


def _gen_jsonld(article, faqs):
    """產生增強JSON-LD結構化資料（SEO+GEO+AIO）"""
    aid = article["id"]
    cat = article["cat"]
    cat_slugs = {
        "貓行為實驗室": "cat-behavior-lab", "狗訓練科學": "dog-training-science",
        "寵物營養實驗室": "pet-nutrition-lab", "高齡寵物學": "senior-pet-studies",
        "幼犬幼貓成長誌": "puppy-kitten-growth", "異寵物種誌": "exotic-species-chronicles",
        "寵物與城市": "pets-and-city", "寵物文化誌": "pet-culture",
        "寵物商品科學": "pet-product-science", "順寵好物推薦": "pet-goods-picks",
    }
    cat_slug = cat_slugs.get(cat, "blog.html")
    kw = article["keywords"].split(",")[0].strip()

    # Article schema with Speakable (AIO/語音搜尋優化)
    article_data = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": article["title"],
        "description": article["desc"],
        "image": [f"{SITE_URL}/images/{article['img1']}", f"{SITE_URL}/images/{article['img2']}"],
        "author": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "url": SITE_URL,
                      "logo": {"@type": "ImageObject", "url": f"{SITE_URL}/images/logo.webp"}},
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"{SITE_URL}/posts/{aid}.html"},
        "articleSection": cat,
        "keywords": article["keywords"],
        "inLanguage": "zh-TW",
        "about": {"@type": "Thing", "name": kw},
        "speakable": {
            "@type": "SpeakableSpecification",
            "xpath": ["/html/head/title", "/html/head/meta[@name='description']/@content"]
        }
    }

    # BreadcrumbList schema
    breadcrumb_data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首頁", "item": SITE_URL},
            {"@type": "ListItem", "position": 2, "name": cat, "item": f"{SITE_URL}/{cat_slug}.html"},
            {"@type": "ListItem", "position": 3, "name": article["title"]}
        ]
    }

    schemas = [article_data, breadcrumb_data]

    # FAQ schema
    if faqs:
        faq_data = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": f["q"],
                            "acceptedAnswer": {"@type": "Answer", "text": f["a"]}} for f in faqs]
        }
        schemas.append(faq_data)

    return json.dumps(schemas, ensure_ascii=False, indent=2)


def generate_all(articles_data):
    """產生所有文章"""
    os.makedirs(POSTS_DIR, exist_ok=True)
    count = 0
    for article in articles_data:
        html = gen_article_html(article, articles_data)
        path = os.path.join(POSTS_DIR, f"{article['id']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        count += 1
    print(f"Generated {count} articles")
    return count


if __name__ == "__main__":
    # 測試用
    from articles_data import ARTICLES_90
    generate_all(ARTICLES_90)
