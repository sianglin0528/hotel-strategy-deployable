import os
from dotenv import load_dotenv
load_dotenv()


import openai

# 使用新版 OpenAI Python SDK
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_chatgpt(user_question, context_text):
    prompt = f"""
你是一位飯店營運顧問。以下是目前預測的住房率與策略資訊：

{context_text}

請根據上面內容，回答這個問題：
{user_question}
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "system", "content": "你是一位專業飯店策略顧問，擅長根據預測資料與競品價格給建議。" },
            { "role": "user", "content": prompt }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
