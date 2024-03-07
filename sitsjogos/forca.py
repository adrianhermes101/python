import jogos

def jogar():

    secreta = "amexa"
    letrasAcertadas = ["_", "_", "_", "_", "_"]
    tentativas = 7

    while tentativas > 0 and "_" in letrasAcertadas:
        palpite = input("Escreva uma letra:").lower()

        if palpite in secreta:
            index = 0
            for letra in secreta:
                if palpite == letra:
                    letrasAcertadas [index] = letra
                index += 1
        else:
            tentativas -= 1
            print(f"Você errou, ainda tem {tentativas} Restantes.")
        print(f"Você acertou uma das letras.{letrasAcertadas}")

    if "_" not in letrasAcertadas:
        print(f"Parabéns, você ganhou Nada")
    else:
        print(f"Que pena, você perdeu. a palavra era {secreta}")
    jogos.escolha_jogo()

if(__name__=="__main__"):
    jogar_forca()