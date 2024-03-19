import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    print("bem vindo camraada")
    print("escolha predra, papel ou tisoura")

    while True:
        print(f"{opcoes}")
        escolha_jogador = input("Sua ecolha:").lower()
        if escolha_jogador not in opcoes:
            print("burro,re-tente")
            continue


        escolha_computador = random.choice(opcoes)
        print(f"computador es colieu: {escolha_computador}") 

        if escolha_jogador == escolha_computador:
            print("empate")
        elif(
            (escolha_jogador == "pedra" and escolha_computador == "tesoura") or
            (escolha_jogador == "tesoura" and escolha_computador == "papel") or
            (escolha_jogador == "papel" and escolha_computador == "pedra") 
            ):
            print("voce ganhou")
        else:
            print("vose perdeu kakaka")
        jogar_novamente = input("quer jogar novamente?").lower()
        if jogar_novamente != "sim":
            break
if __name__ == "__main__":    
    jogar_jokenpo()
