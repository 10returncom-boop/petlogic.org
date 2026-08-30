# PetLogic 毛毛邏輯 寵物知識百科 — 網站規格書

| 項目 | 內容 |
|---|---|
| **版本** | v2.0 |
| **更新日期** | 2026-08-30 |
| **設計規劃開發** | 張書欣 |
| **文件狀態** | 正式版 |

---

## 一、網站基本變數

| 變數名稱 | 值 | 說明 |
|---|---|---|
| `SITE_NAME` | 毛毛邏輯 寵物知識百科 | 網站名稱（顯示用） |
| `SITE_NAME_EN` | PetLogic | 英文品牌名（meta/JSON-LD） |
| `DOMAIN` | https://petlogic.org | 正式網域 |
| `REPO_URL` | https://github.com/10returncom-boop/petlogic.org | GitHub 倉庫 |
| `CONTACT_PHONE` | 0968-222201 | 聯絡電話 |
| `CONTACT_LINE` | 331.today | Line ID |
| `DESIGNER` | 張書欣 | 設計規劃開發者 |
| `SITE_TAGLINE` | 用科學邏輯理解你的毛孩 | 網站標語 |
| `THEME_COLOR` | #2a9d8f | 主題色（teal） |
| `LANGUAGE` | zh-TW | 網站語言 |
| `TOTAL_ARTICLES` | 101 | 文章總數 |
| `TOTAL_CATEGORIES` | 10 | 專欄分類數 |

---

## 二、技術架構

| 項目 | 規格 |
|---|---|
| **託管平台** | GitHub Pages |
| **網站類型** | 靜態 HTML（無後端、無資料庫） |
| **圖片格式** | WebP（全文統一） |
| **動畫格式** | GIF（footer 底圖，10 個分類各一） |
| **CSS** | 單一檔案 `css/style.css` |
| **JavaScript** | 單一檔案 `js/main.js`（下拉選單、年份） |
| **自訂網域** | GoDaddy 註冊，CNAME 指向 GitHub Pages |
| **DNS** | GoDaddy 管理，A 記錄指向 GitHub Pages IP |
| **HTTPS** | GitHub Pages 自動簽發憑證 |
| **部署方式** | git push → GitHub Actions 自動部署 |
| **本機工作目錄** | `C:\Users\SUSI\Doubao\chats\2026-08-27\new-chat-18\petlogic-org` |
| **D 槽鏡像** | `D:\_zoot_webzone\alone\sites\petlogic.org` |
| **備用資料區** | `D:\_WWW\petlogic-備用資料區`（47 檔，不上傳 GitHub） |

---

## 三、10 大專欄分類

| 序號 | 分類名稱 | 檔名 | 圖示 | Header 圖 | Footer GIF |
|---|---|---|---|---|---|
| 1 | 🐱 貓行為實驗室 | `cat-behavior-lab.html` | 🐱 | header-cat-behavior.webp | footer-cat-behavior.gif |
| 2 | 🐕 狗訓練科學 | `dog-training-science.html` | 🐕 | header-dog-training.webp | footer-dog-training.gif |
| 3 | 🥼 寵物營養實驗室 | `pet-nutrition-lab.html` | 🥼 | header-pet-nutrition.webp | footer-pet-nutrition.gif |
| 4 | 🧓 高齡寵物學 | `senior-pet-studies.html` | 🧓 | header-senior-pet.webp | footer-senior-pet.gif |
| 5 | 🌱 幼犬幼貓成長誌 | `puppy-kitten-growth.html` | 🌱 | header-puppy-kitten.webp | footer-puppy-kitten.gif |
| 6 | 🦎 異寵物種誌 | `exotic-species-chronicles.html` | 🦎 | header-exotic-pets.webp | footer-exotic-pets.gif |
| 7 | 🏙️ 寵物與城市 | `pets-and-city.html` | 🏙️ | header-pets-city.webp | footer-pets-city.gif |
| 8 | 📜 寵物文化誌 | `pet-culture.html` | 📜 | header-pet-culture.webp | footer-pet-culture.gif |
| 9 | 🛒 寵物商品科學 | `pet-product-science.html` | 🛒 | header-pet-product.webp | footer-pet-product.gif |
| 10 | 🛍️ 順寵好物推薦 | `pet-goods-picks.html` | 🛍️ | header-default.webp | footer-default.gif |

> 每分類 9 篇文章（post-012 ~ post-101），加上原始 11 篇精選文章（post-001 ~ post-011），共 101 篇。

---

## 四、檔案結構

```
petlogic.org/
├── index.html                  # 首頁
├── blog.html                   # 文章總覽（含搜尋、分類篩選）
├── 404.html                    # 錯誤頁
├── sitemap.xml                 # 網站地圖（103 URL）
├── robots.txt                  # 搜尋引擎規則
├── rss.xml                     # RSS 訂閱
├── CNAME                       # 自訂網域設定
├── .nojekyll                   # 關閉 Jekyll 處理
├── _config.yml                 # GitHub Pages 設定
├── .gitignore                  # 忽略備用資料區
├── README.md                   # 專案說明
│
├── css/
│   └── style.css               # 全部樣式（15.9 KB）
│
├── js/
│   └── main.js                 # 互動邏輯（2.2 KB）
│
├── images/                     # 136 張圖片（全部 WebP/GIF/PNG）
│   ├── favicon.png             # 64×64 瀏覽器圖示
│   ├── apple-touch-icon.png    # 180×180 iOS 圖示
│   ├── logo.webp               # 網站 Logo
│   ├── og-image.webp           # 1200×630 FB/Line 分享預覽圖
│   ├── header-*.webp           # 10 張分類 Header 底圖（無文字）
│   ├── footer-*.gif            # 10 張分類 Footer 動畫底圖
│   ├── hero-post-012~101.webp  # 90 篇文章封面圖
│   ├── article-*.webp          # 11 篇原始文章內文圖
│   ├── category-*.webp         # 分類頁卡片圖
│   └── cat-*.webp / dog-*.webp # 原始文章插圖
│
├── posts/                      # 101 篇文章
│   ├── post-001.html ~ post-011.html   # 原始精選文章
│   └── post-012.html ~ post-101.html   # 90 篇 SEO 文章
│
└── .github/workflows/
    └── deploy.yml              # GitHub Actions 自動部署
```

---

## 五、SEO / GEO / AIO 優化設定

### 5.1 每頁必備 Meta

| 標籤 | 說明 |
|---|---|
| `<title>` | 含主關鍵字 + 長尾字，黑色字體顯示 |
| `<meta name="description">` | 150-160 字元描述，含關鍵字 |
| `<meta name="keywords">` | 5-8 個關鍵字 |
| `<link rel="canonical">` | 規範網址 |
| `<meta property="og:*">` | Facebook/Line 分享標題、描述、圖片 |
| `<meta name="twitter:*">` | Twitter 卡片 |
| `<meta name="robots">` | `index, follow, max-image-preview:large` |

### 5.2 結構化資料（JSON-LD）

| Schema 類型 | 用途 |
|---|---|
| `Organization` | 品牌資訊、Logo、社群連結 |
| `WebSite` | 網站名稱、搜尋行動 |
| `Article` | 每篇文章的作者、日期、圖片 |
| `BreadcrumbList` | 麵包屑導航 |
| `FAQPage` | 常見問題（精選文章） |

### 5.3 圖片 SEO

- 每張圖片皆有 `alt` 屬性，含 SEO 關鍵字與長尾字
- 全部使用 WebP 格式（除 favicon/apple-touch-icon 為 PNG）
- `loading="lazy"` 延遲載入
- 明確標示 `width` / `height` 避免 CLS

### 5.4 內部連結

- 每篇文章關聯 3 篇相關文章
- 首頁 → 分類頁 → 文章頁 三層架構
- Footer 全站導航列（10 分類連結）
- sitemap.xml 提交 Google Search Console

---

## 六、頁面結構規格

### Header（全站統一）
- 背景：`header-{分類}.webp`（無文字漸層底圖）+ 深色半透明覆蓋層
- 左側：`毛毛邏輯 寵物知識百科` 文字連結
- 右側：首頁 / 文章總覽 / 專欄分類（下拉選單，10 分類）
- 高度：自適應內容

### Footer（全站統一，10 分類動畫主題不同）
- 背景：`footer-{分類}.gif` 動畫底圖 + 深色覆蓋層
- 內容：
  - Logo 圖片 + 標語
  - 聯絡：0968-222201
  - Line：331.today
  - © 2026 毛毛邏輯 寵物知識百科 · 設計規劃開發：張書欣
- 分類頁另有四欄式導航（品牌 + 3 個分類連結欄）

### 文章頁模板
- H1：文章標題（黑色字，含核心關鍵字）
- H2/H3：章節標題（SEO 優化，黑色字）
- 每篇 2 張內文圖（與文章最相關，alt 含長尾關鍵字）
- 相關文章推薦（3 篇）
- 無日期顯示

---

## 七、版本變更紀錄

| 版本 | 日期 | 變更重點 |
|---|---|---|
| v1.0 | 2026-08-27 | 網站初始建立：101 篇文章、10 大專欄、SEO/GEO/AIO 基礎優化 |
| v1.1 | 2026-08-28 | 加入 footer 聯絡資訊、5 個網站 Icon、10 張 Header 圖、OG 圖更新 |
| v1.2 | 2026-08-28 | Header 移除文字、site-logo 移除腳印 icon、品牌名改為「毛毛邏輯」 |
| v2.0 | 2026-08-30 | 清理 47 個未使用檔案（14.2 MB）、建立備用資料區、產出正式規格書 |

---

## 八、部署與維運

### 發布流程
```bash
cd C:\Users\SUSI\Doubao\chats\2026-08-27\new-chat-18\petlogic-org
git add -A
git commit -m "說明"
git push origin main
# GitHub Actions 自動部署，約 1-2 分鐘生效
```

### 本機鏡像同步
```bash
robocopy <工作目錄> D:\_zoot_webzone\alone\sites\petlogic.org /MIR
```

### 注意事項
- `備用資料區/` 已加入 `.gitignore`，不會上傳 GitHub
- 圖片統一使用 WebP，新圖需用轉換工具處理
- 新增文章需同步更新 `sitemap.xml`、`rss.xml`、`blog.html`
- DNS 由 GoDaddy 管理，勿隨意變更 nameserver
