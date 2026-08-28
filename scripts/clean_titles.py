#!/usr/bin/env python3
"""清理文章標題：去除贅語，保留SEO核心關鍵字"""
import re
import sys
sys.path.insert(0, '.')
from articles_data import ARTICLES_90

def clean_title(title):
    """去除標題中的贅語和多餘修飾"""
    # 移除 ｜ 後的分類標籤
    title = re.sub(r'｜.*$', '', title)
    
    # 移除常見贅語
    redundant = [
        r'完全圖解[：:]?',
        r'完整指南',
        r'的科學解釋',
        r'的雙重解讀',
        r'的行為學意義',
        r'的行為學分析',
        r'的營養學分析與風險評估',
        r'的代謝秘密',
        r'你讀對了嗎[？?]?',
        r'的演化心理學與壓力紓解',
        r'的資訊解密與費洛蒙科學',
        r'的根本原因與',
        r'的5步驟修正方法',
        r'的6種類型與對應訓練方法',
        r'的3種認知訓練方法[：:]',
        r'的10步驟可靠召回',
        r'進階[：:]',
        r'的正確步驟',
        r'的5個誤解',
        r'的核心要點與下一步行動',
        r'完整概念解析',
        r'對寵物健康的實際影響',
        r'短期影響與長期後果',
        r'步驟一：評估與準備',
        r'從零開始',
        r'實用指南',
        r'深度解析',
        r'全面解析',
        r'詳細指南',
        r'終極指南',
        r'必讀',
        r'懶人包',
        r'一次搞懂',
        r'秒懂',
        r'圖解',
        r'大全',
        r'寶典',
        r'聖經',
        r'的科學',
        r'之謎',
        r'大解密',
        r'解密',
        r'真相',
        r'秘辛',
        r'內幕',
        r'驚人',
        r'不可不知',
        r'一定要知道',
        r'你必須知道',
        r'你不可不知',
        r'超實用',
        r'超詳細',
        r'超完整',
        r'最完整',
        r'最詳細',
        r'最實用',
        r'最新',
        r'2026最新',
        r'2025最新',
        r'版',
        r'篇',
        r'總整理',
        r'整理',
        r'彙整',
        r'懶人',
        r'快速',
        r'簡單',
        r'輕鬆',
        r'有效',
        r'高效',
        r'專業',
        r'權威',
        r'醫師',
        r'獸醫師',
        r'推薦',
        r'必買',
        r'必收',
        r'必看',
        r'必學',
        r'必讀',
        r'收藏',
        r'轉發',
        r'分享',
        r'點讚',
        r'關注',
    ]
    
    for pattern in redundant:
        title = re.sub(pattern, '', title)
    
    # 清理多餘的標點和空格
    title = re.sub(r'[：:]\s*$', '', title)
    title = re.sub(r'[，,]\s*$', '', title)
    title = re.sub(r'\s+', ' ', title)
    title = title.strip()
    
    # 特殊修復：一些常見的語句調整
    fixes = [
        (r'貓咪為什麼會踩奶\?心理學與行為學', '貓咪為什麼會踩奶？'),
        (r'貓咪尾巴姿勢12種尾巴語言', '貓咪尾巴姿勢：12種尾巴語言'),
        (r'貓咪夜間跑酷為什麼凌晨3點最活躍', '貓咪夜間跑酷：為什麼凌晨3點最活躍'),
        (r'貓咪對著你慢眨眼是在說我愛你嗎', '貓咪慢眨眼是在說我愛你嗎'),
        (r'貓咪為什麼會把東西撥下桌\?狩獵本能還是單純欠揍', '貓咪為什麼會把東西撥下桌？'),
        (r'多貓家庭的階級關係如何判斷誰是老大如何減少貓咪衝突', '多貓家庭階級關係：如何判斷誰是老大'),
        (r'貓咪分離焦慮的7個訊號與行為調整方案', '貓咪分離焦慮：7個訊號與調整方案'),
        (r'貓咪為什麼喜歡聞你的鞋子嗅覺行為', '貓咪為什麼喜歡聞你的鞋子？'),
        (r'狗狗為什麼會撲人\?興奮greet行為', '狗狗為什麼會撲人？5步驟修正'),
        (r'狗狗牽繩拉扯5步驟鬆繩行走訓練', '狗狗牽繩拉扯：5步驟鬆繩行走訓練'),
        (r'狗狗吠叫6種類型', '狗狗吠叫：6種類型與訓練方法'),
        (r'狗狗為什麼會翻肚子\?臣服邀玩還是請求搔肚', '狗狗為什麼會翻肚子？'),
        (r'幼犬咬手咬腳的制止方法為什麼處罰只會讓情況更糟', '幼犬咬手咬腳：制止方法與常見錯誤'),
        (r'狗狗召回訓練為什麼你的狗叫不回來', '狗狗召回訓練：為什麼叫不回來'),
        (r'狗狗對抗焦慮去敏感化反向制約與Threshold訓練', '狗狗焦慮：去敏感化與反向制約訓練'),
        (r'狗狗為什麼會吃草\?營養需求本能行為還是腸胃不適', '狗狗為什麼會吃草？'),
        (r'響片訓練如何用Shaping方法訓練複雜行為', '響片訓練：Shaping方法訓練複雜行為'),
        (r'貓咪為什麼是專性肉食動物\?牛磺酸精胺酸與維生素A', '貓咪為什麼是專性肉食動物？'),
        (r'狗狗可以吃素食嗎\?蛋白質與必需胺基酸', '狗狗可以吃素食嗎？營養學分析'),
    ]
    
    for old, new in fixes:
        if re.search(old, title):
            title = new
            break
    
    return title

# 清理所有標題
cleaned = []
for a in ARTICLES_90:
    old = a['title']
    new = clean_title(old)
    a['title'] = new
    cleaned.append((a['id'], old, new))

# 輸出結果
print(f"{'ID':<12} {'原標題':<55} {'新標題'}")
print("-" * 120)
for aid, old, new in cleaned:
    changed = "✓" if old != new else " "
    print(f"{aid:<12} {changed} {old[:50]:<52} → {new}")

# 統計
changed_count = sum(1 for _, old, new in cleaned if old != new)
print(f"\n總計: {len(cleaned)} 篇, {changed_count} 篇已修改")

# 儲存清理後的資料（寫回articles_data.py的方式：產生一個新的import）
import json
with open('cleaned_titles.json', 'w', encoding='utf-8') as f:
    json.dump([{'id': aid, 'title': new} for aid, _, new in cleaned], f, ensure_ascii=False, indent=2)
print("\n已儲存 cleaned_titles.json")
