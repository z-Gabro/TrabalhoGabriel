from projeto1_arvores.BST import BST, No

class AVL(BST):
    def _obter_altura(self, no):
        if not no:
            return 0
        return getattr(no, 'altura', 1)

    def _obter_balanceamento(self, no):
        if not no:
            return 0
        return self._obter_altura(no.esq) - self._obter_altura(no.dir)

    def _rotacao_direita(self, z):
        y = z.esq
        T3 = y.dir
        y.dir = z
        z.esq = T3
        z.altura = 1 + max(self._obter_altura(z.esq), self._obter_altura(z.dir))
        y.altura = 1 + max(self._obter_altura(y.esq), self._obter_altura(y.dir))
        return y

    def _rotacao_esquerda(self, z):
        y = z.dir
        T2 = y.esq
        y.esq = z
        z.dir = T2
        z.altura = 1 + max(self._obter_altura(z.esq), self._obter_altura(z.dir))
        y.altura = 1 + max(self._obter_altura(y.esq), self._obter_altura(y.dir))
        return y

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if not no_atual:
            novo_no = No(valor)
            novo_no.altura = 1
            return novo_no
        elif valor < no_atual.valor:
            no_atual.esq = self._inserir_recursivo(no_atual.esq, valor)
        elif valor > no_atual.valor:
            no_atual.dir = self._inserir_recursivo(no_atual.dir, valor)
        else:
            return no_atual

        no_atual.altura = 1 + max(self._obter_altura(no_atual.esq), self._obter_altura(no_atual.dir))
        balanco = self._obter_balanceamento(no_atual)

        if balanco > 1 and valor < no_atual.esq.valor:
            return self._rotacao_direita(no_atual)
        if balanco < -1 and valor > no_atual.dir.valor:
            return self._rotacao_esquerda(no_atual)
        if balanco > 1 and valor > no_atual.esq.valor:
            no_atual.esq = self._rotacao_esquerda(no_atual.esq)
            return self._rotacao_direita(no_atual)
        if balanco < -1 and valor < no_atual.dir.valor:
            no_atual.dir = self._rotacao_direita(no_atual.dir)
            return self._rotacao_esquerda(no_atual)

        return no_atual

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no_atual, valor):
        no_atual = super()._remover_recursivo(no_atual, valor)
        
        if no_atual is None:
            return no_atual

        no_atual.altura = 1 + max(self._obter_altura(no_atual.esq), self._obter_altura(no_atual.dir))
        balanco = self._obter_balanceamento(no_atual)

        if balanco > 1 and self._obter_balanceamento(no_atual.esq) >= 0:
            return self._rotacao_direita(no_atual)
        if balanco > 1 and self._obter_balanceamento(no_atual.esq) < 0:
            no_atual.esq = self._rotacao_esquerda(no_atual.esq)
            return self._rotacao_direita(no_atual)
        if balanco < -1 and self._obter_balanceamento(no_atual.dir) <= 0:
            return self._rotacao_esquerda(no_atual)
        if balanco < -1 and self._obter_balanceamento(no_atual.dir) > 0:
            no_atual.dir = self._rotacao_direita(no_atual.dir)
            return self._rotacao_esquerda(no_atual)

        return no_atual
        
    def altura(self):
        if self.raiz is None:
            return -1
        return self._obter_altura(self.raiz) - 1