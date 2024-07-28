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
    openai.api_key = OPENAI_API_KEY

