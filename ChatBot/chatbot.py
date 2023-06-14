#Construção de um ChatBot com GPT-4 e Python

#Import
import openai
import os

chave_openai = os.environ.get('key_openai') 

#Chave
openai.api_key = "chave_openai"

#Função para gerar texto a partir do modelo

def gera_texto(texto):

    #Pega reposta
    response = openai.Completion.create(

        #Modelo utilizado
        engine = "text-davinci-003",

        #Texto de inicio de conversa com o chat bot
        prompt = texto,

        #Tamanho da resposta gerada no modelo
        max_tokens = 150,

        #Número de conclusões para cada prompt
        n = 5,


        #O texto não vai conter seq de parada
        stop = None,

        #Medida da aleatoriedade de um texto gerado está entre 0 e 1
        #Valores próximos a 1 indicam que a saída é a mais aleatória e 0 significa que a saída é muito identificável.
        temperature = 0.8
    )

    return response.choices[0].text.strip()