# TrabalhoGabriel

# Estruturas, Pesquisa e Ordenação de Dados

Este repositório contém os projetos desenvolvidos na disciplina **Estruturas, Pesquisa e Ordenação de Dados**, com foco na implementação prática e análise de desempenho de estruturas de dados e algoritmos fundamentais.

---

## Integrantes

- Patrick Guilherme  
- Matheus Nogueira  
- Gabriel da Silva  

---

## Objetivo

O objetivo deste trabalho é aplicar conceitos teóricos na prática, implementando estruturas de dados e algoritmos clássicos, além de analisar seu comportamento por meio de experimentos controlados.

Foram abordados:

- Estruturas de dados em árvore  
- Algoritmos de busca  
- Algoritmos de ordenação  
- Análise de complexidade  
- Comparação entre teoria e prática  

---

## Estrutura do Repositório

TrabalhoGabriel/
│
├── projeto1_arvores/
│ ├── main.py
│ ├── BST.py
│ ├── AVL.py
│ ├── RubroNegra.py
│ └── ...
│
├── projeto2_buscas/
│ ├── main.py
│ ├── algoritmos_busca.py
│ └── ...
│
├── projeto3_ordenacao/
│ ├── main.py
│ ├── algoritmos.py
│ └── ...
│
├── main.py # Menu principal
├── relatorio-final.pdf
└── README.md

---

## Projeto 1 – Estruturas de Árvores

### Implementações

- Árvore Binária de Busca (BST)
- Árvore AVL
- Árvore Rubro-Negra

### Objetivo

Analisar o impacto do balanceamento no desempenho das operações:

- Inserção  
- Busca  
- Remoção  

### Principais Resultados

- BST pode degradar para O(n)  
- AVL mantém balanceamento rigoroso  
- Rubro-Negra apresenta melhor custo-benefício prático  

---

## Projeto 2 – Sistemas de Busca

### Implementações

- Busca Sequencial  
- Busca Binária  
- Busca em Árvore de Busca  

### Objetivo

Comparar o desempenho dos métodos de busca em diferentes cenários.

### Metodologia

- Diferentes volumes de dados  
- Testes de melhor, médio e pior caso  
- Execução múltipla para análise estatística  

### Análise Estatística

- Média do tempo de execução  
- Desvio padrão  

### Resultados

- Busca sequencial → O(n)  
- Busca binária → O(log n)  
- Busca em árvore depende do balanceamento  

---

## Projeto 3 – Algoritmos de Ordenação

### Implementações

- Insertion Sort  
- Quick Sort  

### Objetivo

Avaliar o desempenho dos algoritmos em diferentes cenários.

### Cenários Testados

- Melhor caso (lista ordenada)  
- Caso médio (aleatório)  
- Pior caso (ordem inversa)  

### Resultados

- Insertion Sort eficiente para pequenos dados  
- Quick Sort mais eficiente no geral  
- Sensível à escolha do pivô  

---

## Como Executar

### Pré-requisitos

- Python 3 instalado

---

### Executar menu principal

Na raiz do projeto:

```bash
python main.py
```

### Menu interativo

O sistema exibirá:

===== SISTEMA DE PROJETOS =====
1 - Projeto 1 (Árvores)
2 - Projeto 2 (Buscas)
3 - Projeto 3 (Ordenação)
0 - Sair
Basta escolher o projeto desejado.

### Reprodutibilidade
Os experimentos utilizam semente fixa para garantir consistência:

```bash
random.seed(42)
```

Isso permite que os resultados sejam reproduzidos em diferentes execuções.

### Relatório

O relatório completo contendo:

- Fundamentação teórica
- Metodologia experimental
- Resultados
- Discussões

está disponível em:

relatorio-final.pdf