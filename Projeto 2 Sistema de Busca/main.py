from Arvore import ArvoreBusca
from AlgoritmosBusca import buscaArvoreBusca, buscaBinaria, buscaSequencial

 # Criando a árvore de busca
arvore = ArvoreBusca()

for i in range(1000):
    arvore.inserir(arvore.raiz, i)

# Realizando buscas
valor_procurado = 342
encontrado = buscaArvoreBusca(arvore.raiz, valor_procurado)
print(f"Valor {valor_procurado} encontrado: {encontrado}")