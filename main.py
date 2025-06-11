from openai import OpenAI
import os

client = OpenAI(api_key="")

response = client.chat.completions.create(
    model="gpt-4.1-nano-2025-04-14",
    messages=[
        {"role": "user", "content": "プログラミングを始めたばかりの俺に励ましの言葉をください！"}
        ]
)
print("🍰AIからのメッセージ:")
print(response.choices[0].message.content)