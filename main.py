import os
import openai
from dotenv import load_dotenv

def main():
    # APIkeyの設定
    load_dotenv()
    try:
        OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    except KeyError:
        print("OPENAI_API_KEY environment variable not found. Please make sure it is set.")
        return
    
    openai.api_key = OPENAI_API_KEY

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {
            "role": "system",
            "content": ""
            },
            {
            "role": "user",
            "content": "How are you?"
            }
        ],
        #temperature=1.0,#低くすることで、高い確率の出力が選ばれやすくなり、回答の一貫性が高まる。 確率分布の散らばり具合の調整
        #max_tokens=64,
        #top_p=1 #正確で事実に基づいた回答を求めるのであれば、この値を低く。 上位p%のトークンを取得
    )
    print(response)
    print("\n\n\n")
    print(response["choices"][0]["message"]["content"])
    print("\n\n\n")

if __name__ == "__main__":
    main()