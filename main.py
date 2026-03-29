from projeto1_arvores.main import mainProjeto1 as main_p1
from projeto2_buscas.main import mainProjeto2 as main_p2
from projeto3_ordenacao.main import mainProjeto3 as main_p3


def menu():
    while True:
        print("\n===== SISTEMA DE PROJETOS =====")
        print("1 - Projeto 1 (Árvores)")
        print("2 - Projeto 2 (Buscas)")
        print("3 - Projeto 3 (Ordenação)")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            main_p1()

        elif op == "2":
            main_p2()

        elif op == "3":
            main_p3()

        elif op == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()