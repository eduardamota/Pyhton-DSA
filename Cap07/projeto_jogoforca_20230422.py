import random
from os import system,name

#Função para limpar a tela em cada execução
def limpa_tela():
    
    #Windows
    if name == 'nt':
        _= system('cls') #como retornaria um valor do system, vamos jogar esse valor para o '_'
    else: #mac ou linux
        _=system ('clear')

def game():
    limpa_tela()
    print("\n Olá, seja bem-vindo ao jogo da forca. Divirta-se!")
    print("\n Adivinhe a palavra: \n")

    palavra = open('C:\PythonDSA\Cap07\palavras_jogo.txt','r')
    lista_palavras = palavra.readlines()
    palavra_aleatoria = random.choice(lista_palavras).strip() #O strip vai remover os espaços em branco
    palavra.close()



    letras_descobertas = ['#' for letra in palavra_aleatoria]
    chances = len(palavra_aleatoria) + 1
    letras_erradas = []

    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nNúmeros de chances restantes : ", chances)
        print("Essas são as letras erradas: ",", ".join(letras_erradas))


        while True:
            tentativa = input("Digite uma letra: ").lower()
            if len(tentativa) ==1:
                break
            else:
                print("Digite apenas uma letra")

        if tentativa in palavra_aleatoria:
            index = 0
            for letra in palavra_aleatoria:
                if letra == tentativa:
                    letras_descobertas[index] = letra
                index +=1
        else:
            chances-=1
            letras_erradas.append(tentativa)

        if "#" not in letras_descobertas:
            print("\n Jogo encerrado, você venceu! A palavra era: ",palavra_aleatoria)
            break
    if "#" in letras_descobertas:
        print("Fim de jogo, todas as tentativas foram usadas. A palavra era: ",palavra_aleatoria)


game()
