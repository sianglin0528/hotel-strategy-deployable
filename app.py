
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet
from utils.preprocess import load_and_process_data
from utils.generate_suggestion import generate_suggestion
from utils.chatgpt_reply import ask_chatgpt

st.set_page_config(page_title="飯店營運決策AI助理", layout="centered")

st.title("🏨 飯店營運決策AI助理")
st.markdown("預測住房率 ➜ 自動建議策略 ➜ 助你快速做決策")

df, prophet_df = load_and_process_data("data/hotel_data.csv")

with st.expander("📄 查看原始資料"):
    st.dataframe(df.tail(10))

# 上傳資料
uploaded_file = st.file_uploader("請上傳飯店營運資料（CSV）", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ 資料成功上傳！")
    st.subheader("📊 資料預覽")
    st.dataframe(df.head())

model = Prophet()
model.fit(prophet_df)
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

st.subheader("📈 住房率預測圖（含未來7天）")
fig = model.plot(forecast)
st.pyplot(fig)

latest = forecast.tail(1).iloc[0]
suggestion = generate_suggestion(latest)

st.subheader("💡 系統建議")
st.info(suggestion)

st.subheader("🤖 問我一個問題")
user_input = st.text_input("例如：『我應該調整價格嗎？』")

if user_input:
    context = f"預測住房率為 {latest['yhat']:.2f}，房價為 {df['room_price'].iloc[-1]}，競品價格為 {df['competiter_price'].iloc[-1]}"
    gpt_reply = ask_chatgpt(user_input, context)
    st.success(gpt_reply)





