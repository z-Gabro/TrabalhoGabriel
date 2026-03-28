import random
import time
import statistics
import random

from Arvore import ArvoreBusca
from AlgoritmosBusca import buscaSequencial, buscaBinaria, buscaArvoreBusca


def medir_tempo(funcao, *args, repeticoes=30):
    tempos = []
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        funcao(*args)
        fim = time.perf_counter()
        tempos.append(fim - inicio)
    return tempos


def analisar(nome, tempos):
    media = statistics.mean(tempos)
    desvio = statistics.stdev(tempos)
    print(f"{nome}: média={media:.6f}s | desvio={desvio:.6f}s")


tamanhos = [50000, 500000, 5000000]

for n in tamanhos:
    print(f"\n--- Teste com n = {n} ---")

    lista = list(range(n))
    random.shuffle(lista)
    chave = random.choice(lista)

    # IMPORTANTE: lista ordenada para busca binária
    lista_ordenada = lista.copy()

    # Criar árvore
    arvore = ArvoreBusca()
    for valor in lista:
        arvore.inserir(valor)

    # Medições
    tempos_seq = medir_tempo(buscaSequencial, lista, chave)
    tempos_bin = medir_tempo(buscaBinaria, lista_ordenada, chave)
    tempos_arv = medir_tempo(buscaArvoreBusca, arvore.raiz, chave)

    # Análise
    analisar("Sequencial", tempos_seq)
    analisar("Binária", tempos_bin)
    analisar("Árvore", tempos_arv)