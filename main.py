import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

def talk():
    # OpenAIのAPIを使用して会話を行う
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": "How are you?"}
        ]
    )
    print(response)
    print("\n\n\n")
    print(response.choices[0].message.content)
    print("\n\n\n")

    # 会話機能の実行
    talk()
if __name__ == "__main__":
    main()