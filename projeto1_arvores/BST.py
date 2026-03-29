class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class BST:
    def __init__(self):
        self.raiz = None

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar_recursivo(no.esq, valor)
        return self._buscar_recursivo(no.dir, valor)

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esq is None:
                no.esq = No(valor)
            else:
                self._inserir_recursivo(no.esq, valor)
        elif valor > no.valor:
            if no.dir is None:
                no.dir = No(valor)
            else:
                self._inserir_recursivo(no.dir, valor)

    def altura(self):
        return self._altura_recursiva(self.raiz)

    def _altura_recursiva(self, no):
        if no is None:
            return -1
        return max(self._altura_recursiva(no.esq), self._altura_recursiva(no.dir)) + 1

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esq = self._remover_recursivo(no.esq, valor)
        elif valor > no.valor:
            no.dir = self._remover_recursivo(no.dir, valor)
        else:
            if no.esq is None:
                return no.dir
            elif no.dir is None:
                return no.esq

            temp = self._menor_valor(no.dir)
            no.valor = temp.valor
            no.dir = self._remover_recursivo(no.dir, temp.valor)

        return no

    def _menor_valor(self, no):
        atual = no
        while atual.esq is not None:
            atual = atual.esq
        return atual

    # --- MÉTODOS DE PERCURSO ---
    def percorrer_em_ordem(self):
        elementos = []
        self._percorrer_em_ordem_recursivo(self.raiz, elementos)
        return elementos

    def _percorrer_em_ordem_recursivo(self, no, elementos):
        if no:
            self._percorrer_em_ordem_recursivo(no.esq, elementos)
            elementos.append(no.valor)
            self._percorrer_em_ordem_recursivo(no.dir, elementos)

    def percorrer_pre_ordem(self):
        elementos = []
        self._percorrer_pre_ordem_recursivo(self.raiz, elementos)
        return elementos

    def _percorrer_pre_ordem_recursivo(self, no, elementos):
        if no:
            elementos.append(no.valor)
            self._percorrer_pre_ordem_recursivo(no.esq, elementos)
            self._percorrer_pre_ordem_recursivo(no.dir, elementos)