from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
   organization=os.environ["ORGANIZATION"],
   project=os.environ["PROJECT"],
   api_key=os.environ["API_KEY"]
)

messages = [
    {"role": "system", "content": "Você é um assistente muito prestativo, e ajuda em duvidas simples dentro de uma escola."},
]

input_message = input("Esperando input: ")
messages.append({"role": "user", "content": input_message})

while input_message != 'fim':
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=200
    )
    answer = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    print("Resposta: ", answer)
    
    input_message = input("Esperando input: ")
    messages.append({"role": "user", "content": input_message})
