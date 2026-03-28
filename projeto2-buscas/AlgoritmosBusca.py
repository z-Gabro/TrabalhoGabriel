def buscaSequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1

def buscaBinaria(lista, chave):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

def buscaArvoreBusca(arvore, chave):
    if arvore is None:
        return False

    if chave == arvore.valor:
        return True
    elif chave < arvore.valor:
        return buscaArvoreBusca(arvore.esquerda, chave)
    else:
        return buscaArvoreBusca(arvore.direita, chave)