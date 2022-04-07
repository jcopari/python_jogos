import random as rd

def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem-vindo ao jogo da forca!***")
    print("*********************************")

def jogo():

    imprime_mensagem_abertura()

    arquivo =open("frutas.txt", 'r', encoding='utf-8')
    palavras = []
    for linha in arquivo:
        linha = linha.upper()
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    escolhida = rd.randrange(0,len(palavras))

    palavra_secreta = palavras[escolhida]
    #aqui está outro jeito de definir variáveis
    #enforcou, acertou = False, False

    #descontinuarei essa "palavra secreta
    #palavra_secreta = "banana".upper() #converter direto a str para uppercase
    #Agora quero que apareça algo do tipo "_ _ _ _ _" para o jogagor
    #E que ele guarde as letras acertadas. Então terei de usar uma lista
    letras_acertadas = list("_" * len(palavra_secreta))
    #list("_" * len(palavra_secreta)) Assim eu crio uma lista de acordo com o tamanho da palavra secreta
    #Poderia também fazer x = ["_" for letras in palavra_secreta]
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erro = 0

    while(not enforcou and not acertou):

        #Quero tratar algumas questões que podem aparecer
        #Por exemplo: entradas com espaço ou a diferença
        #Entre maiúsculas e minúsculas. Usarei alguns métododos
        chute = input("Chute uma letra: ")
        chute = chute.strip().upper() #método para tirar espaços somado ao upper

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    #print("Encontrei a letra {} na posição {}".format(letra.upper(), index))
                    letras_acertadas[index] = letra
                index += 1
            print(letras_acertadas)
        else:
            erro +=1
            desenha_forca(erro)

        enforcou = erro == 7
        acertou = "_" not in letras_acertadas

        if(acertou):
            imprime_mensagem_vencedor()
        elif(enforcou):
            imprime_mensagem_perdedor(palavra_secreta)

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if(__name__ == "__main__"):
     jogo()