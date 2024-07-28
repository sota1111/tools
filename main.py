import os
from openai import OpenAI
import pandas as pd
import numpy as np
from ast import literal_eval
from dotenv import load_dotenv
from utils.embeddings_utils import get_embedding, cosine_similarity

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

# search through the reviews for a specific product
def search_reviews(df, product_description, n=3, pprint=True):
    product_embedding = get_embedding(
        product_description,
        model="text-embedding-3-small"
    )
    df["similarity"] = df.embedding.apply(lambda x: cosine_similarity(x, product_embedding))

    results = (
        df.sort_values("similarity", ascending=False)
        .head(n)
        .combined.str.replace("Title: ", "")
        .str.replace("; Content:", ": ")
    )
    if pprint:
        for r in results:
            print(r[:200])
            print()
    return results

def main():    
    # 会話機能の実行
    talk()

    # データの読み込み
    datafile_path = "data/fine_food_reviews_with_embeddings_1k.csv"
    df = pd.read_csv(datafile_path)
    df["embedding"] = df.embedding.apply(literal_eval).apply(np.array)
    
    # レビュー検索機能の実行
    print("Searching for 'delicious beans' reviews...")
    search_reviews(df, "delicious beans", n=3)

if __name__ == "__main__":
    main()