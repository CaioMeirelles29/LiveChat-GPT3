import openai
from get_env import print_env

env = print_env(["app_key"])

#Configuração de ambiente

openai.api_key = env["app_key"]

# Model_engine

model_engine = "text-davinci-003"

while True:
    print(50*"-")
    prompt = input("Escreva algo: ")
    print(50*"-")
    print("O GPT está processando sua mensagem...")
    
#Configuração de geração de resposta

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        temperature = 0.7,
    )

    response = completion.choices[0].text
    print(response)

    saída = input("Deseja sair do Chat? ")
    if saída == "sim":
        break



