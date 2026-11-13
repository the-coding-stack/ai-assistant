from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
MODEL = os.getenv("MODEL")

client = OpenAI(
    base_url=BASE_URL,
    api_key=API_KEY
)

messages = []

messages.append(
    {
        "role": "system", 
        "content": "Acts like a very humble and helpful assistant. Always responds in a polite and respectful manner and respond under 100 words. If you don't know the answer, say 'I don't know' instead of making up an answer."
    }
)

while True:

    user_input = input("Vivek: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        break


    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )

    print("Assistant: ", response.choices[0].message.content)

    messages.append({"role": "assistant", "content": response.choices[0].message.content})

