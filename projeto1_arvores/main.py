from BST import BST
from AVL import AVL
from RubroNegra import RubroNegra
from Caixeiro import realizar_experimentos
import random

def relatorio_arvore(arvore, nome):
    print(f"\n--- RELATÓRIO: {nome} ---")
    # Gera 10 números aleatórios únicos entre 1 e 100 para o teste
    valores_teste = random.sample(range(1, 101), 10)
    
    print(f"1. Inserindo os valores aleatórios: {valores_teste}")
    for v in valores_teste:
        arvore.inserir(v)

    print(f"2. Percurso em Pré-Ordem (Raiz, Esq, Dir): {arvore.percorrer_pre_ordem()}")
    print(f"3. Percurso em Ordem (Valores ordenados): {arvore.percorrer_em_ordem()}")
    print(f"4. Altura da árvore atual: {arvore.altura()}")
    
    # Escolhe um valor aleatório da lista para buscar e outro para remover
    # Isso garante que as operações sempre encontrarão um alvo válido
    valores_para_operacoes = random.sample(valores_teste, 2)
    busca_val = valores_para_operacoes[0]
    remover_val = valores_para_operacoes[1]
    
    resultado = arvore.buscar(busca_val)
    print(f"5. Buscando valor {busca_val}: {'Encontrado' if resultado else 'Não encontrado'}")
    
    print(f"6. Removendo o valor: {remover_val}")
    arvore.remover(remover_val)
    
    print(f"7. Percurso em Pré-Ordem após remoção: {arvore.percorrer_pre_ordem()}")
    print(f"8. Percurso em Ordem após remoção: {arvore.percorrer_em_ordem()}")
    print(f"9. Altura após a remoção: {arvore.altura()}")
    print("-" * 30 + "\n")

def main():
    while True:
        print("====== MENU DO TRABALHO ======")
        print("1. Testar Árvore Binária de Busca (BST)")
        print("2. Testar Árvore AVL")
        print("3. Testar Árvore Rubro-Negra")
        print("4. Executar Experimentos Caixeiro-Viajante")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        # O "match" em Python funciona como o "switch case" de outras linguagens
        match opcao:
            case "1":
                relatorio_arvore(BST(), "Árvore Binária de Busca (BST)")
            case "2":
                relatorio_arvore(AVL(), "Árvore AVL")
            case "3":
                relatorio_arvore(RubroNegra(), "Árvore Rubro-Negra")
            case "4":
                realizar_experimentos()
            case "0":
                print("Encerrando programa...")
                break
            case _:
                print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
