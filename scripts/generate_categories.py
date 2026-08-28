#!/usr/bin/env python3
"""
PetLogic 分類頁面產生器（架構C：主題專欄型）
用法: python generate_categories.py
產生 9 個專欄頁面到網站根目錄
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIES = [
    {
        "slug": "cat-behavior-lab",
        "name": "🐱 貓行為實驗室",
        "short": "貓行為實驗室",
        "icon": "🐱",
        "desc": "用實驗觀察與行為學研究，解讀貓咪每個動作背後的邏輯。不教你「怎麼訓練貓」，而是告訴你「貓為什麼這樣做」。",
        "keywords": "貓咪行為,貓咪心理,貓咪實驗,貓咪認知,貓行為學,貓咪溝通",
        "posts": [
            {"file": "post-001.html", "title": "實驗：把貓咪單獨留在家8小時，攝影機拍到的6個意外行為", "excerpt": "我們在5個貓家庭安裝攝影機，記錄貓咪獨處時的真實行為。結果發現，多數貓咪不是在睡覺……", "img": "article-cat-alone-home.webp", "date": "2026-08-25", "read": "12 分鐘"},
            {"file": "post-002.html", "title": "貓咪呼噜聲的頻率（25-150Hz）真的能促進骨骼癒合嗎？", "excerpt": "傳說貓咪呼噜有治癒力。我們查閱了12篇研究，測量了3隻貓的呼噜頻率，結果發現……", "img": "article-cat-purring.webp", "date": "2026-08-18", "read": "9 分鐘"},
        ],
        "topics": ["貓咪認知實驗", "貓咪情緒解碼", "貓咪溝通方式", "多貓互動", "貓咪環境豐容", "貓咪壓力偵測", "貓咪學習能力", "貓咪記憶研究"]
    },
    {
        "slug": "dog-training-science",
        "name": "🐕 狗訓練科學",
        "short": "狗訓練科學",
        "icon": "🐕",
        "desc": "從操作制約到認知心理學，用科學方法理解狗狗的學習機制。每個訓練技巧都有理論依據，不搞經驗論。",
        "keywords": "狗狗訓練,正向訓練,狗心理學,操作制約,響片訓練,狗狗學習",
        "posts": [
            {"file": "post-003.html", "title": "響片 vs 口語標記：12隻狗的學習速度對比實驗", "excerpt": "響片訓練真的比口語好嗎？我們設計了一個簡單的學習任務，讓12隻狗分別用兩種方式學習……", "img": "article-dog-clicker-training.webp", "date": "2026-08-22", "read": "10 分鐘"},
        ],
        "topics": ["操作制約理論", "正向強化實踐", "響片訓練科學", "狗狗認知實驗", "社會化研究", "問題行為處遇", "狗狗情緒識別", "訓練誤區拆解"]
    },
    {
        "slug": "pet-nutrition-lab",
        "name": "🥼 寵物營養實驗室",
        "short": "寵物營養實驗室",
        "icon": "🥼",
        "desc": "飼料成分實測、營養素代謝機制、飲食爭議的科學驗證。用數據說話，不跟風營養迷思。",
        "keywords": "寵物營養,貓狗飲食,飼料成分,寵物食品實測,營養素,寵物飲食科學",
        "posts": [
            {"file": "post-004.html", "title": "市售10款貓糧成分實測：標榜無穀卻檢出穀物的品牌是？", "excerpt": "我們買了10款標榜「無穀」的貓糧，送檢穀物成分。結果有3款檢出小麥或玉米DNA……", "img": "article-cat-food-test.webp", "date": "2026-08-20", "read": "14 分鐘"},
        ],
        "topics": ["飼料成分實測", "營養素代謝", "食材爭議驗證", "鮮食vs乾糧", "過敏飲食研究", "腎病飲食科學", "寵物肥胖機制", "補劑功效驗證"]
    },
    {
        "slug": "senior-pet-studies",
        "name": "🧓 高齡寵物學",
        "short": "高齡寵物學",
        "icon": "🧓",
        "desc": "老貓老狗的身體變化、認知衰退、慢性疾病管理與安寧照護。以生命品質為核心的高齡照護專欄。",
        "keywords": "高齡貓,高齡犬,老貓照護,老狗照護,寵物認知障礙,寵物安寧,寵物老化",
        "posts": [
            {"file": "post-005.html", "title": "狗狗癡呆（CCD）的5個早期訊號與家庭評估量表", "excerpt": "狗狗也會得阿茲海默？認知障礙症候群（CCD）影響超過一半的10歲以上狗狗。早期發現可以減緩惡化……", "img": "article-senior-dog-dementia.webp", "date": "2026-08-15", "read": "11 分鐘"},
        ],
        "topics": ["認知障礙研究", "關節炎管理", "慢性腎病照護", "高齡營養需求", "安寧照護倫理", "疼痛評估工具", "高齡環境改造", "生命品質量表"]
    },
    {
        "slug": "puppy-kitten-growth",
        "name": "🌱 幼犬幼貓成長誌",
        "short": "幼犬幼貓成長誌",
        "icon": "🌱",
        "desc": "從出生到成年的發育里程碑系列。以時間軸追蹤幼犬幼貓的身體、行為與認知發育，每個階段都有科學依據。",
        "keywords": "幼犬發育,幼貓發育,幼犬照顧,幼貓照顧,寵物社會化,幼犬幼貓",
        "posts": [
            {"file": "post-006.html", "title": "幼犬0-12週發育里程碑：每週的行為變化與關鍵任務", "excerpt": "從閉眼的新生兒到好奇的探索者，幼犬的前12週決定了一生。我們整理了每週的發育重點……", "img": "article-puppy-development.webp", "date": "2026-08-12", "read": "13 分鐘"},
        ],
        "topics": ["新生兒期發育", "社會化黃金期", "疫苗時間軸", "斷奶與營養", "認知發育階段", "乳牙與恆齒", "早期訓練", "發育異常辨識"]
    },
    {
        "slug": "exotic-species-chronicles",
        "name": "🦎 異寵物種誌",
        "short": "異寵物種誌",
        "icon": "🦎",
        "desc": "每種異寵的深度物種檔案：自然棲地、行為生態、人工飼養的環境參數與常見誤區。不是飼養指南，是物種全紀錄。",
        "keywords": "異寵,爬蟲,兔子,倉鼠,寵物鳥,另類寵物,異寵物種",
        "posts": [
            {"file": "post-007.html", "title": "豹紋守宮物種誌：沙漠晝行性的迷思與飼養參數的科學依據", "excerpt": "大家都說豹紋守宮是夜行性，但最新的野外觀察研究發現……牠們其實在黃昏最活躍。這徹底改變了燈光配置。", "img": "article-leopard-gecko.webp", "date": "2026-08-10", "read": "12 分鐘"},
        ],
        "topics": ["物種分類與棲地", "野外行為生態", "環境參數科學", "常見誤區拆解", "繁殖與基因", "異寵健康管理", "法律與保育", "物種比較研究"]
    },
    {
        "slug": "pets-and-city",
        "name": "🏙️ 寵物與城市",
        "short": "寵物與城市",
        "icon": "🏙️",
        "desc": "帶寵物在城市生活的公共空間、交通、法規與社會觀察。從大眾運輸到寵物公園設計，用城市規劃的視角看寵物。",
        "keywords": "寵物友善城市,帶寵旅行,寵物公共空間,寵物運輸,寵物法規,城市養寵",
        "posts": [
            {"file": "post-008.html", "title": "寵物公園設計學：為什麼大多數狗公園其實對狗不友善", "excerpt": "全台超過200個寵物公園，但多數只是「圍起來的草地」。動物行為學家指出，這些設計可能反而增加狗狗衝突……", "img": "article-dog-park-design.webp", "date": "2026-08-08", "read": "10 分鐘"},
        ],
        "topics": ["大眾運輸規則", "寵物公園設計", "租屋與寵物", "帶寵通勤", "公共空間權益", "城市寵物數據", "災難應變", "社區共融"]
    },
    {
        "slug": "pet-culture",
        "name": "📜 寵物文化誌",
        "short": "寵物文化誌",
        "icon": "📜",
        "desc": "寵物在歷史、文學、藝術與當代社會中的角色。用文化研究的視角，理解人類為什麼離不開毛孩。",
        "keywords": "寵物文化,寵物歷史,人寵關係,寵物藝術,寵物社會學,動物與文化",
        "posts": [
            {"file": "post-009.html", "title": "從神廟到沙發：貓咪如何用4000年征服人類家庭", "excerpt": "從古埃及的神聖貓到中世紀的巫女伴侶，再到現代的網紅貓——貓咪的地位經歷了戲劇性的轉變。", "img": "article-cat-history-temple-sofa.webp", "date": "2026-08-05", "read": "11 分鐘"},
        ],
        "topics": ["寵物歷史演變", "人寵關係社會學", "寵物與文學藝術", "寵物經濟現象", "寵物迷因文化", "動物倫理學", "跨文化寵物觀", "寵物與宗教"]
    },
    {
        "slug": "pet-product-science",
        "name": "🛒 寵物商品科學",
        "short": "寵物商品科學",
        "icon": "🛒",
        "desc": "用科學方法檢驗寵物商品：成分分析、材質安全、功能實測、性價比拆解。買之前先看數據，不被行銷話術綁架。",
        "keywords": "寵物商品,寵物用品,貓砂評測,飼料評比,寵物玩具安全,寵物商品實測",
        "posts": [
            {"file": "post-010.html", "title": "市售8款貓砂除臭力對比實驗：活性炭、沸石、酵素誰最有效？", "excerpt": "我們用氨氣偵測儀在密閉空間測試8款貓砂的除臭效果，結果最貴的那款竟然排第三……", "img": "article-cat-litter-comparison.webp", "date": "2026-08-28", "read": "10 分鐘"},
        ],
        "topics": ["貓砂材質科學", "飼料標籤解讀", "玩具安全材質", "洗毛精成分分析", "窩墊支撐力測試", "電子用品安全", "項圈牽繩強度", "性價比拆解"]
    },
    {
        "slug": "pet-goods-picks",
        "name": "🛍️ 順寵好物推薦",
        "short": "順寵好物推薦",
        "icon": "🛍️",
        "desc": "用過才敢推！從貓砂到飼料、從玩具到窩墊，每樣都是小編親自試用後的真心推薦。不業配、不說謊，只推真的好用的。",
        "keywords": "寵物好物推薦,貓咪用品推薦,狗狗用品推薦,寵物用品開箱,順寵好物,寵物必買清單",
        "posts": [
            {"file": "post-011.html", "title": "「我家貓主子用過都說讚」——2026年最值得買的10樣寵物好物（不業配版）", "excerpt": "小編家3貓2狗親自試用半年，篩出10樣真的離不開的好物。從200塊的貓砂盆到2000塊的餵食器，樣樣都是血汗錢換來的真實心得。", "img": "article-pet-products-recommendation.webp", "date": "2026-08-29", "read": "8 分鐘"},
        ],
        "topics": ["貓咪用品開箱", "狗狗用品推薦", "高CP值好物", "飼主真心推薦", "踩雷避雷區", "新手必買清單", "智慧寵物用品", "季節限定好物"]
    },
]

# 下拉選單 HTML（用於所有頁面）
DROPDOWN_HTML = '''<div class="dropdown">
        <button class="dropbtn" onclick="toggleDropdown()">專欄分類 <span class="arrow">▼</span></button>
        <div class="dropdown-content" id="catDropdown">
          <div class="dropdown-header"><span>10大專欄 · 深度知識</span><a href="blog.html#all-posts" class="view-all">查看全部 →</a></div>
          <div class="dropdown-grid">
            <a href="cat-behavior-lab.html" class="dropdown-item"><span class="di-name">🐱 貓行為實驗室</span><span class="di-desc">實驗觀察解讀貓行為</span></a>
            <a href="dog-training-science.html" class="dropdown-item"><span class="di-name">🐕 狗訓練科學</span><span class="di-desc">學習理論與訓練實踐</span></a>
            <a href="pet-nutrition-lab.html" class="dropdown-item"><span class="di-name">🥼 寵物營養實驗室</span><span class="di-desc">成分實測與營養機制</span></a>
            <a href="senior-pet-studies.html" class="dropdown-item"><span class="di-name">🧓 高齡寵物學</span><span class="di-desc">老貓老狗照護研究</span></a>
            <a href="puppy-kitten-growth.html" class="dropdown-item"><span class="di-name">🌱 幼犬幼貓成長誌</span><span class="di-desc">發育里程碑時間軸</span></a>
            <a href="exotic-species-chronicles.html" class="dropdown-item"><span class="di-name">🦎 異寵物種誌</span><span class="di-desc">物種深度檔案</span></a>
            <a href="pets-and-city.html" class="dropdown-item"><span class="di-name">🏙️ 寵物與城市</span><span class="di-desc">公共空間與法規</span></a>
            <a href="pet-culture.html" class="dropdown-item"><span class="di-name">📜 寵物文化誌</span><span class="di-desc">歷史社會與文化</span></a>
            <a href="pet-product-science.html" class="dropdown-item"><span class="di-name">🛒 寵物商品科學</span><span class="di-desc">商品實測與成分分析</span></a>
            <a href="pet-goods-picks.html" class="dropdown-item"><span class="di-name">🛍️ 順寵好物推薦</span><span class="di-desc">用過才敢推的真心清單</span></a>
          </div>
        </div>
      </div>'''

# 文章頁用的下拉選單（路徑多一層 ../）
DROPDOWN_HTML_POST = DROPDOWN_HTML.replace('href="', 'href="../')

HEADER_TEMPLATE = '''<header class="site-header" style="background-image:linear-gradient(rgba(15,25,35,0.6),rgba(15,25,35,0.75)),url('images/header-{header_theme}.webp');">
  <div class="header-inner">
    <a href="index.html" class="site-logo"><span class="paw">🐾</span>PetLogic 寵物知識百科</a>
    <nav class="site-nav">
      <a href="index.html">🏠 首頁</a>
      <a href="blog.html">📚 文章總覽</a>
      {dropdown}
      <a href="index.html#about">關於</a>
    </nav>
  </div>
</header>'''

def get_footer_html(theme="default"):
    """產生帶有動畫GIF底圖的footer"""
    return f'''<footer class="site-footer footer-animated" style="background-image:url('images/footer-{theme}.gif');">
  <div class="footer-overlay">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="images/logo.webp" alt="PetLogic 寵物知識百科 logo" class="footer-logo" style="max-width:180px;height:auto;margin-bottom:10px;">
        <p>用科學邏輯理解毛孩，讓每一位飼主都能安心養寵。10大深度專欄，持續更新中。</p>
      </div>
      <div class="footer-col">
        <h4>行為與訓練</h4>
        <a href="cat-behavior-lab.html">🐱 貓行為實驗室</a>
        <a href="dog-training-science.html">🐕 狗訓練科學</a>
        <a href="puppy-kitten-growth.html">🌱 成長誌</a>
      </div>
      <div class="footer-col">
        <h4>健康、營養與好物</h4>
        <a href="pet-nutrition-lab.html">🥼 營養實驗室</a>
        <a href="senior-pet-studies.html">🧓 高齡寵物學</a>
        <a href="pet-product-science.html">🛒 商品科學</a>
        <a href="pet-goods-picks.html">🛍️ 好物推薦</a>
      </div>
      <div class="footer-col">
        <h4>文化與生活</h4>
        <a href="exotic-species-chronicles.html">🦎 異寵物種誌</a>
        <a href="pets-and-city.html">🏙️ 寵物與城市</a>
        <a href="pet-culture.html">📜 寵物文化誌</a>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-links">
        <a href="index.html">首頁</a><a href="blog.html">文章總覽</a><a href="sitemap.xml">網站地圖</a><a href="rss.xml">RSS</a>
      </div>
      <p style="margin-bottom:6px;">聯絡：0968-222201 &nbsp;|&nbsp; Line：331.today</p>
      <p>© <span id="current-year">2026</span> PetLogic 寵物知識百科 · 設計規劃開發：張書欣 · 內容僅供參考，醫療問題請諮詢獸醫師</p>
    </div>
  </div>
  </div>
</footer>
<script src="js/main.js"></script>'''

# 分類對應footer主題
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


def generate_category_page(cat):
    posts_html = ""
    for p in cat["posts"]:
        posts_html += f'''      <a href="posts/{p["file"]}" class="post-card" data-cat="{cat["short"]}">
        <img src="images/{p["img"]}" class="post-card-thumb" alt="{p["title"]}" loading="lazy">
        <div class="post-card-body">
          <span class="post-card-cat">{cat["name"]}</span>
          <h3 class="post-card-title">{p["title"]}</h3>
          <p class="post-card-excerpt">{p["excerpt"]}</p>
          <div class="post-card-meta"><span>閱讀 {p["read"]}</span></div>
        </div>
      </a>
'''

    topics_html = ""
    for t in cat["topics"]:
        topics_html += f'        <span style="display:inline-block;background:white;border:1px solid var(--border);padding:6px 16px;border-radius:20px;font-size:0.88rem;color:var(--text-light);margin:4px;">{t}</span>\n'

    footer_theme = CAT_FOOTER_THEME.get(cat["short"], "default")
    header = HEADER_TEMPLATE.format(dropdown=DROPDOWN_HTML, header_theme=footer_theme)
    footer = get_footer_html(footer_theme)

    html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{cat["name"]} | PetLogic 寵物知識百科</title>
<meta name="description" content="{cat["desc"]}">
<meta name="keywords" content="{cat["keywords"]}">
<meta name="author" content="PetLogic 寵物知識百科">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#2a9d8f">
<meta property="og:title" content="{cat["name"]} | PetLogic 寵物知識百科">
<meta property="og:description" content="{cat["desc"]}">
<meta property="og:type" content="website">
<meta property="og:locale" content="zh_TW">
<meta property="og:site_name" content="PetLogic 寵物知識百科">
<meta property="og:url" content="https://petlogic.org/{cat["slug"]}.html">
<meta property="og:image" content="https://petlogic.org/images/og-image.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{cat["name"]} | PetLogic">
<meta name="twitter:description" content="{cat["desc"]}">
<link rel="canonical" href="https://petlogic.org/{cat["slug"]}.html">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"CollectionPage","name":"{cat["name"]}","description":"{cat["desc"]}","url":"https://petlogic.org/{cat["slug"]}.html"}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"首頁","item":"https://petlogic.org"}},{{"@type":"ListItem","position":2,"name":"{cat["name"]}"}}]}}
</script>
<meta name="google-site-verification" content="YOUR_GSC_VERIFICATION_CODE">
</head>
<body>
{header}
<main class="container" style="padding-top:24px;">
  <div class="post-grid">
{posts_html}  </div>
</main>
{footer}
</body>
</html>'''
    return html


def main():
    count = 0
    for cat in CATEGORIES:
        filepath = os.path.join(BASE_DIR, f"{cat['slug']}.html")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generate_category_page(cat))
        print(f"  ✓ {cat['slug']}.html")
        count += 1
    print(f"\n完成！共產生 {count} 個專欄頁面")


if __name__ == "__main__":
    main()
