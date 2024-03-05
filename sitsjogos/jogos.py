import forca
import adivinhacao

def escolha_jogo():
    print("******")
    print("**escolha o jogo")
    print("******")
    print("(1)forca,(2)adivinhacao")
    jogo = print int(input("qual jogo escolhestes?"))
    if (jogo == 1):
        print("escolheste o jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhacao")
        adivinhacao.jogar()

if(__name__== "__name__"):
    escolhe_jogar()