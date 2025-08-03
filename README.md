
# 🏨 飯店營運決策助理（Hotel Strategy Assistant）

這是一個結合時間序列預測與生成式 AI 的一頁式決策輔助網站，專為飯店經理人設計。使用者可以快速查看住房率趨勢、獲得經營建議，甚至透過 ChatGPT 詢問決策問題。

## 🔍 專案功能

- 📈 使用 Prophet 預測未來住房率
- 📊 顯示住房率趨勢圖（含未來 7 天）
- 💡 系統根據預測數據自動產出策略建議
- 🤖 整合 ChatGPT，可輸入問題獲得個性化決策建議
- 🌐 Streamlit 一頁式網站展示

## 📁 專案結構

```
hotel-strategy-demo/
├── app.py                      # Streamlit 主程式
├── data/
│   └── hotel_data.csv          # 假資料（含日期、住房數、價格等）
├── model/
│   └── （保留位置）
├── utils/
│   ├── preprocess.py           # 資料預處理
│   ├── generate_suggestion.py  # 規則型策略建議
│   └── chatgpt_reply.py        # GPT API 回覆模組
├── requirements.txt            # 安裝依賴
└── README.md                   # 本說明文件
```

## 🚀 如何使用

### 1. 安裝套件

```bash
pip install -r requirements.txt
```

### 2. 執行網站

```bash
streamlit run app.py
```

### 3. 啟用 ChatGPT 問答（可選）

請將你的 OpenAI API 金鑰貼入 `chatgpt_reply.py`：

```python
client = openai.OpenAI(api_key="your-api-key")
```

## 🧠 範例問題

- 「這週是否應該調整房價？」
- 「競品價格影響我多少？」
- 「住房率偏低怎麼辦？」
- Streamlit Demo : https://hotel-strategy-deployable0723.streamlit.app/

---

本專案由 [徐香琳] 開發，融合飯店管理知識與 AI 技術，適合展示於資料分析、AI 應用、產品設計等面試場景。
