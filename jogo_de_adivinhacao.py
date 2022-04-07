

def jogo():
    import random as rd
    print('Jogo de advinhação')
    print('\n*******************')


    #total_de_tentativas = 3 --> Vou botar esta variável antes do "for"
    #rodada = 1

    # while(rodada <= total_de_tentativas):
    #      print(f'Tentativa {rodada} de {total_de_tentativas}')
    #      numero_secreto = 42
    #      numero_escolhido = int(input("Digite um número: "))
    #
    #     ##input recebe números como String
    #     ##precisei fazer uma conversão explícita
    #     ##Posso fazer uma variável para usar em IF, ELIF
    #
    #     #print(f'Você digitou: {numero_escolhido}')
    #
    #     #if(numero_secreto == numero_escolhido):
    #         #print('Você acertou')
    #     #else:
    #         #print('Você errou!')
    #
    #      acerto = numero_escolhido == numero_secreto
    #      maior  = numero_escolhido  > numero_secreto
    #      menor  = numero_escolhido <  numero_secreto
    #
    #      if(acerto):
    #          print('Você acertou')
    #          break
    #      elif(maior):
    #         print('Você errou. O seu número escolhido foi maior que o número secreto')
    #      elif(menor):
    #          print('Você errou. O seu número é menor!')
    #
    #      rodada = rodada + 1

    #Agora tentativa com FOR
                  #range cria um array
                                    #20           #10           #5
    print("Escolha a dificuldade", 'Facil = 1', 'Médio - 2', 'Difícil - 3', sep="\n")
    dificuldade = int(input("Digite o número da dificuldade: "))

    # if(dificuldade == 1):
    #     chance = range(1,21)
    # elif(dificuldade == 2):
    #     chance = range(1,11)    #Desse jeito NÃO certo, no entanto, não é a melhor opção.
    # elif(dificuldade == 3):     #TypeError: 'int' object is not iterable - tive que criar um range(1, total_tentativas+1)
    #     chance = range(1,6)
    #
    # total_de_tentativas = chance
    # rodada = 1
    pontos = 1000
    total_tentativas = 0
    rodada = 1

    if(dificuldade == 1):
        total_tentativas = 20
    elif(dificuldade == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas+1): #range(1,4): #range(start, stop, [step])
         print(f'Tentativa {rodada} de {total_tentativas}')
         #aleatorio = round(int((rd.random()*100))) random() gera entre 0 e 100,então isto é problemático
         aleatorio = rd.randrange(1, 101) #randrange() é justamente para colocarmos valor inicial e final
         numero_secreto = aleatorio
         numero_escolhido = int(input("Digite um número entre 1 e 100:"))

         if(numero_escolhido < 1 or numero_escolhido > 100):
             print("Você deve escolher um número entre 1 e 100")
             continue #continue pula para próxima rodada

         acerto = numero_escolhido == numero_secreto
         maior  = numero_escolhido  > numero_secreto
         menor  = numero_escolhido <  numero_secreto

         # if(acerto):                          #adicionarei sistema de pontuação por rodada
         #     print('Você acertou')
         #     break
         # else:
         #    elif(maior):
         #        print('Você errou. O seu número escolhido foi maior que o número secreto')
         #    elif(menor):
         #        print('Você errou. O seu número é menor!')

         if(acerto):
             print(f'Você acertou! \n')
             break
         else:
             if(maior):
                 print(f"Seu número é maior.")
             elif(menor):
                 print(f"Seu número é menor.")
         pontos_perdidos = abs(numero_secreto - numero_escolhido)
         pontos = pontos - pontos_perdidos

    print(f'Você tem {pontos}')
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogo()

