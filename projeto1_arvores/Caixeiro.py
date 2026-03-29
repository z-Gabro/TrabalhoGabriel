import random
import time
import statistics

def vizinho_mais_proximo_basico(distancias):
    n = len(distancias)          
    visitados = [False] * n      
    
    rota = [0]                   
    visitados[0] = True          
    custo_total = 0              
    cidade_atual = 0             

   
    for _ in range(n - 1):
        distancia_minima = float('inf') 
        proxima_cidade = -1             


        for vizinho in range(n):
           
            if not visitados[vizinho] and vizinho != cidade_atual:
                
               
                if distancias[cidade_atual][vizinho] < distancia_minima:
                    distancia_minima = distancias[cidade_atual][vizinho] 
                    proxima_cidade = vizinho                            

      
        rota.append(proxima_cidade)
        visitados[proxima_cidade] = True
        custo_total += distancia_minima
        cidade_atual = proxima_cidade 

   
    custo_total += distancias[cidade_atual][0]
    rota.append(0)

    return custo_total, rota

def gerar_grafo_aleatorio(n):
    """Gera uma matriz de distâncias simétrica para n cidades."""
    grafo = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = random.randint(10, 100)
            grafo[i][j] = dist
            grafo[j][i] = dist
    return grafo

def realizar_experimentos():
    tamanhos = [10, 50, 100] 
    execucoes = 30           
    
    print("Iniciando experimentos do Caixeiro-Viajante (Vizinho Mais Próximo)\n" + "-"*65)
    
    for tamanho in tamanhos:
        custos, tempos = [], []
        
        for _ in range(execucoes):
            grafo = gerar_grafo_aleatorio(tamanho)
            
            inicio = time.perf_counter()
            custo, _ = vizinho_mais_proximo_basico(grafo)
            fim = time.perf_counter()
            
            custos.append(custo)
            tempos.append(fim - inicio)
            
        print(f"Tamanho da Entrada: {tamanho} Cidades")
        print(f"  -> Custo Médio: {statistics.mean(custos):.2f} | Desvio Padrão: {statistics.stdev(custos):.2f}")
        print(f"  -> Tempo Médio de Execução: {statistics.mean(tempos):.6f} segundos\n")

if __name__ == "__main__":
    realizar_experimentos()