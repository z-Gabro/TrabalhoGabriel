import random
import time
import statistics

def gerar_casos(n):
    random.seed(40)

    melhor = list(range(n))
    pior = list(range(n, 0, -1))

    medio = list(range(n))
    random.shuffle(medio)

    return melhor, medio, pior

def medir_tempo(func, arr):
    inicio = time.perf_counter()
    func(arr.copy())
    fim = time.perf_counter()
    return fim - inicio

def testar_algoritmo(nome, func, tamanhos, repeticoes = 10):
    print(nome)

    for n in tamanhos:
        melhor, medio, pior = gerar_casos(n)

        for caso_nome, lista in [
            ('Melhor: ', melhor),
            ('Médio: ', medio),
            ('Pior: ', pior),
        ]:
            tempos = []

            for _ in range(repeticoes):
                tempos.append(medir_tempo(func, lista))

            media = statistics.mean(tempos)

            print(f"Tamanho {n} | {caso_nome}: {media:.6f} s")
