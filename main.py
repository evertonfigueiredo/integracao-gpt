from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
#    organization=os.environ["ORGANIZATION"],
#    project=os.environ["PROJECT"],
   api_key=os.environ["API_KEY"]
)

messages = [
    {
        "role": "system",
        "content": (
            "Você é um assistente especializado na criação de redações conforme o modelo do ENEM. "
            "Sua tarefa é gerar redações completas baseadas no tema fornecido, seguindo os critérios "
            "de pontuação indicados. Você deve estruturar o texto com introdução, desenvolvimento e conclusão, "
            "considerando os aspectos exigidos pela matriz de competências do ENEM. "
            "Se um usuário solicitar uma redação com nota específica, adapte o texto para refletir essa pontuação. "
            "Utilize argumentos sólidos, coerência textual e evite erros gramaticais. "
            "Se necessário, apresente propostas de intervenção viáveis e detalhadas. "
        ),
    }
]


input_message = input("Esperando input: ")
messages.append({"role": "user", "content": input_message})

while input_message != 'fim':
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=1500
    )
    answer = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": answer})
    print("Resposta: ", answer)
    
    input_message = input("Esperando input: ")
    messages.append({"role": "user", "content": input_message})
