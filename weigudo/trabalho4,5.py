def gravar_lista(lista):
    nome_arq = input("Digite o nome do arquivo: ")
    with open(nome_arq, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "\n")
    print(f"Arquivo gravado com sucesso: {nome_arq}")

def main():
    lista = []

    while True:
        print("O que você deseja fazer?")
        print("1. Inserir um novo item na lista")
        print("2. Excluir um item da lista")
        print("3. Mostrar a lista atual")
        print("4. Sair do programa")
        print("5. Gravar lista em um arquivo")

        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == "1":
            novo_item = input("Digite o novo item: ")
            lista.append(novo_item)
            print("Item adicionado à lista.")
            print("Lista atualizada:", lista)
        elif opcao == "2":
            if not lista:
                print("A lista está vazia.")
            else:
                item_para_excluir = input("Digite o item que deseja excluir: ")
                if item_para_excluir in lista:
                    lista.remove(item_para_excluir)
                    print("Item removido da lista.")
                    print("Lista atualizada:", lista)
                else:
                    print("Item não encontrado na lista.")
        elif opcao == "3":
            if not lista:
                print("A lista está vazia.")
            else:
                print("Lista atual:", lista)
        elif opcao == "4":
            print("Saindo do programa...")
            break
        elif opcao == "5":
            if not lista:
                print("A lista está vazia. Não há nada para gravar.")
            else:
                gravar_lista(lista)
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
