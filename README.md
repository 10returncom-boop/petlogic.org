# PetLogic 寵物知識百科

> 用科學邏輯理解你的毛孩

[![Deploy to GitHub Pages](https://github.com/petlogic-org/petlogic.org/actions/workflows/deploy.yml/badge.svg)](https://github.com/petlogic-org/petlogic.org/actions/workflows/deploy.yml)

## 網站資訊

- **網域**：https://petlogic.org
- **託管**：GitHub Pages
- **技術架構**：靜態 HTML + CSS + WebP 圖片
- **文章數**：101 篇
- **專欄數**：10 大深度專欄

## 10 大專欄

| 專欄 | 說明 |
|---|---|
| 🐱 貓行為實驗室 | 用實驗與觀察拆解貓咪行為 |
| 🐕 狗訓練科學 | 正向訓練的證據與方法 |
| 🥼 寵物營養實驗室 | 飼料實測與營養科學 |
| 🧓 高齡寵物學 | 老貓老狗的照護與醫學 |
| 🌱 幼犬幼貓成長誌 | 0-12個月的發育里程碑 |
| 🦎 異寵物種誌 | 爬蟲、兔、倉鼠的物種科學 |
| 🏙️ 寵物與城市 | 公共空間、法規與城市養寵 |
| 📜 寵物文化誌 | 人寵關係的歷史與社會觀察 |
| 🛒 寵物商品科學 | 用品與食品的成分與效果實測 |
| 🛍️ 順寵好物推薦 | 用過才敢推的真心清單 |

## SEO / GEO / AIO 優化

- **JSON-LD 結構化資料**：Article、BreadcrumbList、FAQPage、Speakable、Organization、WebSite
- **GEO 內容元素**：核心定義框、關鍵數據框、研究來源引用
- **圖片 SEO**：100% 圖片含 alt 屬性，WebP 格式
- **內部連結**：每篇平均 15+ 個內部連結
- **robots.txt**：放行 GPTBot、ClaudeBot、PerplexityBot 等 AI 爬蟲
- **Sitemap**：103 個 URL
- **RSS Feed**：最新 20 篇文章

## 本地開發

```bash
# 產生文章頁面
cd scripts
python master_generate.py

# 預覽（用任意靜態伺服器）
python -m http.server 8080
# 瀏覽器打開 http://localhost:8080
```

## 部署

推送到 `main` 分支後，GitHub Actions 自動部署到 GitHub Pages。

## 自訂網域 DNS 設定

在網域註冊商新增以下 DNS 紀錄：

| 類型 | 主機 | 值 |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | username.github.io |

## 授權

MIT License
