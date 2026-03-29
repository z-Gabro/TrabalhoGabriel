from projeto3_ordenacao.algoritmos import insertion_sort, quick_sort
from projeto3_ordenacao.benchmark import testar_algoritmo

tamanhos = [1000, 5000, 10000]
def mainProjeto3():
    testar_algoritmo("Insertion: ", insertion_sort, tamanhos)
    testar_algoritmo("Quick: ", quick_sort, tamanhos)

if __name__ == "__main__":
    mainProjeto3()