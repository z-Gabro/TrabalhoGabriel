from algoritmos import insertion_sort, quick_sort
from benchmark import testar_algoritmo

tamanhos = [1000, 5000, 10000]

testar_algoritmo("Insertion: ", insertion_sort, tamanhos)
testar_algoritmo("Quick: ", quick_sort, tamanhos)