print("*********************************")
print("********Seja bem-vindo!**********")
print("*********************************")

print("\nEscolha seu jogo")
print("Adivinhação(1) ou Forca(2)")
jogo = int(input("Selecione seu jogo: "))

# if(jogo == 1):                    SERIA O SUFICIENTE, MAS VOU TENTAR DE OUTRA MANEIRA.
#       import forca                E USANDO FUNÇÕES
# elif(jogo == 2):
#       import jogo_de_adivinhacao
# else:
#       print("\nNão existe esse jogo!")
import forca
import jogo_de_adivinhacao

if(jogo == 2):
      print("Iniciando Forca")
      forca.jogo()
elif(jogo == 1):
      print("Iniciando Adivinhação\n")
      jogo_de_adivinhacao.jogo()