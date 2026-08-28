#!/usr/bin/env python3
"""
PetLogic 90篇文章Master產生器
結合所有文章資料，產生文章HTML、更新分類頁、blog、sitemap
"""
import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from articles_data import ARTICLES_90 as A1
from articles_data_2 import ARTICLES_63 as A2
from articles_data_3 import ARTICLES_36 as A3
from seo_article_generator import generate_all, gen_article_html

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS_DIR = os.path.join(BASE_DIR, "posts")
SITE_URL = "https://petlogic.org"

# 合併所有文章
ALL_ARTICLES = A1 + A2 + A3

import re

def clean_title(title):
    """去除標題贅語，保留SEO核心關鍵字"""
    # 移除 ｜ 後的分類標籤
    title = re.sub(r'｜.*$', '', title)
    
    # 移除常見贅語片語（長的先移除）
    patterns = [
        r'的完整照護指南', r'完整照護指南', r'的完整指南', r'完整指南',
        r'的完整評估', r'完整評估', r'的完整清單', r'完整清單',
        r'的完整管理', r'完整管理', r'的完整比較', r'完整比較',
        r'的完整評比', r'完整評比', r'的完整步驟', r'完整步驟',
        r'的科學解釋', r'的科學依據', r'的科學證據', r'科學減重方案',
        r'的雙重解讀', r'的行為學意義', r'的行為學分析', r'的行為學區分',
        r'的營養學分析與風險評估', r'的營養學爭議', r'的營養學',
        r'的代謝秘密', r'的秘密', r'完全圖解[：:]?', r'完全解讀[：:]?',
        r'你讀對了嗎[？?]?', r'怎麼看才不會被騙',
        r'的根本原因與', r'進階[：:]', r'全指南[：:]', r'全台比對[：:]',
        r'的真實案例與防護', r'的實際應用指南', r'的選擇比較',
        r'的管理指南', r'的社會學分析', r'的社會學觀察',
        r'的文化現象', r'的社會意義', r'的市場規模',
        r'的效果比較', r'的優缺點', r'的檢測數據',
        r'的耐用度與貓咪偏好研究', r'對關節的影響比較', r'的拉力測試',
        r'的演化心理學與壓力紓解', r'的資訊解密與費洛蒙科學',
        r'的5個訊號與行為調整方案', r'的6種類型與對應訓練方法',
        r'的3種認知訓練方法[：:]', r'的10步驟可靠召回',
        r'的5步驟修正方法', r'的正確步驟',
        r'的科學與', r'的科學', r'之謎', r'大解密', r'解密',
        r'真相', r'秘辛', r'內幕', r'驚人',
        r'不可不知', r'一定要知道', r'你必須知道', r'你不可不知',
        r'超實用', r'超詳細', r'超完整', r'最完整', r'最詳細', r'最實用',
        r'必買', r'必收', r'必看', r'必學', r'必讀',
        r'深度解析', r'全面解析', r'詳細指南', r'終極指南',
        r'懶人包', r'一次搞懂', r'秒懂', r'圖解', r'大全', r'寶典',
        r'總整理', r'整理', r'彙整', r'快速', r'簡單', r'輕鬆',
        r'有效', r'高效', r'專業', r'權威',
        r'的5個容易被忽略的疼痛訊號與管理',
        r'的症狀與管理', r'的症狀、藥物治療與生活品質管理',
        r'的症狀、診斷與家庭管理', r'從飲食到皮下輸液',
        r'如何幫助適應與居家環境改造',
        r'體重下降食慾增加的警訊與治療選擇',
        r'如何在最後階段維持生命品質',
        r'為什麼老狗半夜走來走去與認知功能的關聯',
        r'品質生活量表',
        r'3-14週應該接觸的100種事物',
        r'為什麼2-7週是貓咪性格的定型期',
        r'核心疫苗、非核心疫苗與抗體力價檢測',
        r'FVRCP、狂犬病與絛蟲預防時間軸',
        r'4-8週的餵食計畫與注意事項',
        r'狩獵練習、同窩互動與咬合力控制',
        r'如何避免創傷經驗與建立終身信心',
        r'從小建立獨處能力的5個實用方法',
        r'哪些「可愛」行為其實是健康警訊',
        r'UVB、溫度梯度與食性',
        r'黃金鼠、三線鼠、老公公鼠的個性與照護差異',
        r'為什麼兔子需要24小時不斷進食與盲腸便',
        r'為什麼多數綠鬣蜥活不過3年與正確飼養方法',
        r'保溫燈、UVB與冬眠',
        r'為什麼不能單獨飼養蜜袋鼯與群居照護',
        r'加熱墊、熱點與隱藏窩的重要性與常見錯誤',
        r'鸚鵡的語言理解、工具使用與情緒智力',
        r'哪些症狀需要立刻就醫（爬蟲、兔、嚙齒類）',
        r'台鐵高鐵捷運公車的規定與注意事項',
        r'如何找到寵物友善租屋與簽約注意事項',
        r'哪個公園對狗最友善與使用注意事項',
        r'從適應外出籠到旅館選擇',
        r'牽繩規定、排泄物清理與攻擊事件的責任歸屬',
        r'全台連鎖與獨立餐廳的寵物政策比對',
        r'噪音、空間與鄰居關係',
        r'Uber Pet、寵物專車與獸醫接送',
        r'小公寓如何讓貓咪不無聊與滿足狩獵需求',
        r'從LOLcats到Nyan Cat',
        r'從招財貓到貓站長、貓島',
        r'從牧羊犬到搜救犬、導盲犬的人狗合作演變',
        r'火化、紀念花園與寵物墓園',
        r'人寵關係翻轉',
        r'從衣服到生日派對的消費文化',
        r'從愛倫坡到村上春樹，貓如何成為作家的繆思',
        r'從忠犬小八到海底總動員，狗狗形象的文化演變',
        r'專家說的和你以為的為什麼不一樣',
        r'活性炭、沸石、酵素與銀離子',
        r'SLS、防腐劑、香精哪些對皮膚有害與安全選擇',
        r'乳膠、橡膠、尼龍的耐咬度與毒性',
        r'餵食器飲水機除蚤項圈',
        r'瓦楞紙、劍麻、木頭的耐用度',
        r'記憶棉、乳膠、棉花',
        r'尼龍、皮質、戰術編織',
        r'酵素、生物製劑與化學除臭劑',
        r'餵食器攝影機被駭',
        r'開放式封閉式自動鏟屎機',
        r'馬達噪音、濾芯成本與清潔難度',
        r'雙電源防卡糧與App功能',
        r'畫質夜視雙向語音與零食投擲',
        r'穩定性高度材質與貓咪接受度',
        r'記憶棉Orthopedic與大型犬支撐力',
        r'指甲剪梳子電剪的安全性與實用性',
        r'透氣性安全性航空公司認證與舒適度',
        r'成分營養價值適口性與價格帶',
    ]
    
    for p in patterns:
        title = re.sub(p, '', title)
    
    # 清理標點
    title = re.sub(r'[：:]\s*$', '', title)
    title = re.sub(r'[，,]\s*$', '', title)
    title = re.sub(r'、\s*$', '', title)
    title = re.sub(r'\s+', ' ', title)
    title = title.strip(' ：:，,、')
    
    # 常見語句修復
    title = title.replace('的與', '與')
    title = title.replace('與與', '與')
    title = re.sub(r'[？?]\s*$', '？', title) if '？' in title or '?' in title else title
    
    return title

# 精確標題覆蓋（SEO優化，去贅語）
TITLE_OVERRIDES = {
    "post-012": "貓咪為什麼會踩奶？行為學解析",
    "post-013": "貓咪尾巴姿勢：12種尾巴語言解讀",
    "post-014": "貓咪為什麼喜歡鑽紙箱？空間偏好心理學",
    "post-015": "貓咪夜間跑酷：為什麼凌晨3點最活躍",
    "post-016": "貓咪慢眨眼是在說我愛你嗎？表情行為學",
    "post-017": "貓咪為什麼會把東西撥下桌？狩獵本能解析",
    "post-018": "多貓家庭階級關係：如何判斷誰是老大",
    "post-019": "貓咪分離焦慮：7個訊號與調整方案",
    "post-020": "貓咪為什麼喜歡聞你的鞋子？嗅覺行為解析",
    "post-021": "狗狗為什麼會撲人？5步驟修正方法",
    "post-022": "狗狗牽繩拉扯：5步驟鬆繩行走訓練",
    "post-023": "狗狗吠叫：6種類型與訓練方法",
    "post-024": "狗狗為什麼會翻肚子？行為學解析",
    "post-025": "幼犬咬手咬腳：制止方法與常見錯誤",
    "post-026": "狗狗召回訓練：為什麼叫不回來",
    "post-027": "狗狗焦慮訓練：去敏感化與反向制約",
    "post-028": "狗狗為什麼會吃草？營養與本能解析",
    "post-029": "響片訓練：Shaping方法訓練複雜行為",
    "post-030": "貓咪為什麼是專性肉食動物？營養學解析",
    "post-031": "狗狗可以吃素食嗎？營養學分析",
    "post-032": "寵物食品標籤怎麼看：成分表與保證值",
    "post-033": "貓咪泌尿道結石與飲食：pH值與水分",
    "post-034": "寵物肥胖：為什麼超過50%的寵物過重",
    "post-035": "生肉飲食BARF：好處、風險與科學證據",
    "post-036": "寵物食品防腐劑與添加劑：安全與風險",
    "post-037": "老貓老狗營養需求：腎臟、關節與認知",
    "post-038": "寵物食物過敏：診斷與處方飼料選擇",
    "post-039": "老貓認知障礙CDS：症狀與家庭管理",
    "post-040": "高齡犬關節炎：5個疼痛訊號與管理",
    "post-041": "老貓慢性腎病CKD：分期與飲食管理",
    "post-042": "高齡寵物聽力視力退化：適應與環境改造",
    "post-043": "老狗瓣膜性心臟病：症狀與治療",
    "post-044": "高齡貓甲狀腺機能亢進：症狀與治療",
    "post-045": "寵物安寧照護Hospice：生命品質管理",
    "post-046": "高齡寵物睡眠變化：認知功能關聯",
    "post-047": "寵物臨終判斷與安樂死時機",
    "post-048": "幼犬社會化關鍵期：3-14週發展指南",
    "post-049": "幼貓社會化與行為發育：2-7週定型期",
    "post-050": "幼犬疫苗接種時間軸：核心疫苗與抗體",
    "post-051": "幼貓疫苗與驅蟲：FVRCP與狂犬病",
    "post-052": "幼犬斷奶與固體食物過渡：4-8週餵食",
    "post-053": "幼貓遊戲行為發展：狩獵練習與咬合力",
    "post-054": "幼犬恐懼期8-11週：如何避免創傷",
    "post-055": "幼貓分離焦慮預防：建立獨處能力",
    "post-056": "幼犬幼貓發育異常辨識：健康警訊",
    "post-057": "鬃獅蜥飼養：UVB、溫度與食性",
    "post-058": "倉鼠品種比較：黃金鼠、三線鼠、老公公鼠",
    "post-059": "兔子消化道生理：為什麼需要24小時進食",
    "post-060": "綠鬣蜥飼養誤區：為什麼多數活不過3年",
    "post-061": "陸龜溫度與光照需求：保溫燈與UVB",
    "post-062": "蜜袋鼯社會需求：為什麼不能單獨飼養",
    "post-063": "蛇類飼養環境配置：加熱墊與隱藏窩",
    "post-064": "鳥類認知能力：鸚鵡語言與工具使用",
    "post-065": "異寵常見急症：哪些症狀需要立刻就醫",
    "post-066": "大眾運輸帶寵物規則：台鐵高鐵捷運公車",
    "post-067": "租屋族養寵：寵物友善租屋與簽約注意",
    "post-068": "台北市寵物公園地圖與評比",
    "post-069": "帶貓旅行準備清單：外出籠與旅館選擇",
    "post-070": "城市遛狗法律責任：牽繩與排泄物規定",
    "post-071": "寵物友善餐廳：全台連鎖與獨立餐廳比對",
    "post-072": "公寓養大型犬：噪音、空間與鄰居關係",
    "post-073": "寵物計程車與接送服務：Uber Pet比較",
    "post-074": "都市貓室內環境豐容：小公寓狩獵需求",
    "post-075": "貓咪如何成為網際網路統治者",
    "post-076": "日本貓文化：招財貓、貓站長與貓島",
    "post-077": "狗狗工作歷史：牧羊犬、搜救犬與導盲犬",
    "post-078": "寵物殯葬文化興起：火化與紀念花園",
    "post-079": "為什麼現代人叫自己貓奴狗奴？",
    "post-080": "寵物時尚產業崛起：衣服與生日派對消費",
    "post-081": "文學中的貓：從愛倫坡到村上春樹",
    "post-082": "電影中的狗狗：從忠犬小八到海底總動員",
    "post-083": "寵物心理學大眾迷思：專家說的和你以為的",
    "post-084": "貓砂除臭機制：活性炭、沸石與酵素比較",
    "post-085": "寵物洗毛精成分解讀：SLS與防腐劑",
    "post-086": "寵物玩具材質安全：乳膠、橡膠與尼龍",
    "post-087": "寵物電子用品電磁輻射與安全性",
    "post-088": "貓抓板材質比較：瓦楞紙、劍麻與木頭",
    "post-089": "寵物窩墊支撐力測試：記憶棉與乳膠",
    "post-090": "寵物項圈與牽繩強度標準：尼龍與皮質",
    "post-091": "寵物除臭噴霧成分：酵素與化學除臭劑",
    "post-092": "智慧寵物用品資安風險：餵食器被駭案例",
    "post-093": "貓砂盆推薦：開放式、封閉式與自動鏟屎機",
    "post-094": "寵物飲水機推薦：馬達噪音與濾芯成本比較",
    "post-095": "自動餵食器推薦：雙電源與App功能比較",
    "post-096": "寵物攝影機推薦：畫質、夜視與雙向語音",
    "post-097": "貓跳台推薦：穩定性、高度與材質比較",
    "post-098": "狗窩推薦：記憶棉與大型犬支撐力",
    "post-099": "寵物美容工具推薦：指甲剪、梳子與電剪",
    "post-100": "寵物外出包推薦：透氣性與航空公司認證",
    "post-101": "貓糧推薦：成分、營養價值與適口性比較",
}

# 應用標題清理
for art in ALL_ARTICLES:
    aid = art["id"]
    if aid in TITLE_OVERRIDES:
        art["title"] = TITLE_OVERRIDES[aid]
    else:
        art["title"] = clean_title(art["title"])

# 使用每篇文章的專屬hero圖片
from download_and_update_images import IMAGE_MAP
for art in ALL_ARTICLES:
    aid = art["id"]
    if aid in IMAGE_MAP:
        art["img1"] = f"hero-{aid}.webp"
        art["img2"] = f"hero-{aid}.webp"  # 第二張也用專屬圖

# 設定日期（依ID順序分配）
base_date = datetime(2026, 9, 1)
for i, art in enumerate(ALL_ARTICLES):
    if "date" not in art:
        art["date"] = (base_date + __import__('datetime').timedelta(days=i)).strftime("%Y-%m-%d")
    if "read_time" not in art:
        art["read_time"] = f"{6 + (i % 5)} 分鐘"

print(f"Total articles: {len(ALL_ARTICLES)}")

# 1. 產生所有文章HTML
print("\n=== 產生文章HTML ===")
os.makedirs(POSTS_DIR, exist_ok=True)
for art in ALL_ARTICLES:
    html = gen_article_html(art, ALL_ARTICLES)
    path = os.path.join(POSTS_DIR, f"{art['id']}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
print(f"Generated {len(ALL_ARTICLES)} articles")

# 2. 產生sitemap.xml
print("\n=== 產生sitemap.xml ===")
sitemap_urls = [f"{SITE_URL}/", f"{SITE_URL}/blog.html", f"{SITE_URL}/404.html"]
# 分類頁
categories = set(a["cat"] for a in ALL_ARTICLES)
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
for slug in cat_slugs.values():
    sitemap_urls.append(f"{SITE_URL}/{slug}.html")
# 文章頁
for art in ALL_ARTICLES:
    sitemap_urls.append(f"{SITE_URL}/posts/{art['id']}.html")

sitemap_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
'''
for url in sitemap_urls:
    sitemap_xml += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
sitemap_xml += '</urlset>'

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)
print(f"Sitemap: {len(sitemap_urls)} URLs")

# 3. 產生RSS
print("\n=== 產生RSS ===")
recent = sorted(ALL_ARTICLES, key=lambda x: x.get("date", ""), reverse=True)[:20]
rss_items = ""
for art in recent:
    rss_items += f'''    <item>
      <title>{art["title"]}</title>
      <link>{SITE_URL}/posts/{art["id"]}.html</link>
      <description>{art["desc"]}</description>
      <category>{art["cat"]}</category>
    </item>
'''
rss_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>PetLogic 寵物知識百科</title>
    <link>{SITE_URL}</link>
    <description>用科學邏輯理解你的毛孩</description>
    <language>zh-TW</language>
{rss_items}  </channel>
</rss>'''
with open(os.path.join(BASE_DIR, "rss.xml"), "w", encoding="utf-8") as f:
    f.write(rss_xml)
print(f"RSS: {len(recent)} recent articles")

# 4. 產生分類頁
print("\n=== 產生分類頁 ===")
from generate_categories import CATEGORIES, generate_category_page

# 更新每個分類的文章列表
import re
for cat in CATEGORIES:
    cat_name = re.sub(r'[^\u4e00-\u9fff\w]', '', cat["name"])  # 移除emoji和符號
    cat_articles = [a for a in ALL_ARTICLES if re.sub(r'[^\u4e00-\u9fff\w]', '', a["cat"]) == cat_name]
    # 轉換為generate_categories需要的格式
    cat["posts"] = []
    for a in cat_articles:
        cat["posts"].append({
            "file": f"{a['id']}.html",
            "title": a["title"],
            "excerpt": a["desc"][:80] + "...",
            "read": a.get("read_time", "8 分鐘"),
            "img": a["img1"]
        })
    html = generate_category_page(cat)
    slug = cat_slugs.get(cat_name, cat_name)
    path = os.path.join(BASE_DIR, f"{slug}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  {cat_name}: {len(cat_articles)} articles -> {slug}.html")

# 5. 產生blog.html（全部文章列表）
print("\n=== 產生blog.html ===")
all_sorted = sorted(ALL_ARTICLES, key=lambda x: x.get("date", ""), reverse=True)
blog_cards = ""
for a in all_sorted:
    blog_cards += f'''    <a href="posts/{a["id"]}.html" class="post-card" data-cat="{a["cat"]}">
      <img src="images/{a["img1"]}" class="post-card-thumb" alt="{a["title"]}" loading="lazy">
      <div class="post-card-body">
        <span class="post-card-cat">{a.get("icon", "📝")} {a["cat"]}</span>
        <h3 class="post-card-title">{a["title"][:60]}</h3>
        <p class="post-card-excerpt">{a["desc"][:70]}...</p>
        <div class="post-card-meta"><span>閱讀 {a.get("read_time", "8 分鐘")}</span></div>
      </div>
    </a>
'''

blog_html = f'''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>全部文章 | PetLogic 寵物知識百科</title>
<meta name="description" content="PetLogic 全部{len(ALL_ARTICLES)}篇寵物科學文章，涵蓋貓行為、狗訓練、營養、高齡寵物、異寵、寵物商品等10大專欄。">
<meta name="keywords" content="寵物知識,貓咪行為,狗狗訓練,寵物營養,高齡寵物,異寵飼養,寵物商品,寵物百科">
<link rel="canonical" href="{SITE_URL}/blog.html">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" type="image/webp" href="images/logo.webp">
</head>
<body>
<header class="site-header" style="background-image:linear-gradient(rgba(15,25,35,0.6),rgba(15,25,35,0.75)),url('images/header-default.webp');">
  <div class="container header-inner">
    <a href="index.html" class="logo">🐾 PetLogic</a>
    <nav class="nav-links"><a href="index.html">首頁</a><a href="blog.html">全部文章</a><a href="rss.xml">RSS</a></nav>
  </div>
</header>
<main class="container" style="padding-top:24px;">
  <div class="post-grid">
{blog_cards}  </div>
</main>
<footer class="site-footer footer-animated" style="background-image:url('images/footer-default.gif');">
<div class="footer-overlay">
<div class="container footer-content">
<div class="footer-brand">
<img src="images/logo.webp" alt="PetLogic 寵物知識百科 logo" class="footer-logo" style="max-width:180px;height:auto;margin-bottom:10px;">
<p>用科學邏輯理解你的毛孩 · 共{len(ALL_ARTICLES)}篇文章</p>
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

with open(os.path.join(BASE_DIR, "blog.html"), "w", encoding="utf-8") as f:
    f.write(blog_html)
print(f"Blog: {len(all_sorted)} articles listed")

print("\n=== 全部完成 ===")
print(f"總文章數: {len(ALL_ARTICLES)}")
print(f"分類頁: {len(CATEGORIES)}")
print(f"Sitemap URLs: {len(sitemap_urls)}")
