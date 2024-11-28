from math import sqrt
from funcoes_auxiliares import print_mapa
from funcoes_auxiliares import print_caminho
import heapq

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    
    # dimensões
    linhas, colunas = len(grid), len(grid[0])
    
    # movimentos possíveis
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # fila com os nós que devem ser visitados
    queue = [(0, pos_inicial)] # (prioridade, nó)



    # matriz de visitados
    visited = [[False] * colunas for _ in range(linhas)] 
    
    # dicionário com predecessores de cada nó visitado
    pred = {}

    while queue:

        # extraindo o custo e o proximo nó
        custo, (x, y) = heapq.heappop(queue)

        # print(f'({x}, {y})')
        # tesouro encontado
        if (x, y) == pos_tesouro:
            caminho = []
            pos_atual = pos_tesouro

            # montagem do caminho usando os predecessores de cada nó
            while pos_atual:
                caminho.append(pos_atual)
                pos_atual = pred.get(pos_atual)
            
            # retorna o caminho
            return caminho[::-1]

        if visited[x][y]:
            continue

        # marcando como visitado
        visited[x][y] = True 

        # explorando vizinhos
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy

            # verifica se o vizinho ta dentro da matriz
            if 0 <= nx < linhas and 0 <= ny < colunas and not visited[nx][ny]:

                if grid[x][y] == '#':
                    continue
                elif grid[nx][ny] == '.':  # Célula vazia
                    step_cost = 1
                elif grid[nx][ny] == 'L':  # Lama
                    step_cost = 5
                elif grid[nx][ny] == 'T':  # Tesouro
                    step_cost = 0
                else:
                    continue

                novo_custo = custo + step_cost

                # Atualiza se o caminho for válido
                if (nx, ny) not in pred or novo_custo < custo:
                    pred[(nx, ny)] = (x, y)  # Rastreia o caminho
                    heapq.heappush(queue, (novo_custo, (nx, ny)))

    return []

def busca_gulosa(grid, pos_inicial, pos_tesouro):

    def h(x):  # distancia de manhattan
        return abs(pos_tesouro[0] - x[0]) + abs(pos_tesouro[1] - x[1])


    # dimensões
    linhas, colunas = len(grid), len(grid[0])
    
    # movimentos possíveis
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # fila com os nós que devem ser visitados
    queue = [(h(pos_inicial), pos_inicial)] # (prioridade, nó)



    # matriz de visitados
    visited = [[False] * colunas for _ in range(linhas)] 
    
    # dicionário com predecessores de cada nó visitado
    pred = {}

    while queue:

        # extraindo o custo e o proximo nó
        custo, (x, y) = heapq.heappop(queue)

        # print(f'({x}, {y})')
        # tesouro encontado
        if (x, y) == pos_tesouro:
            caminho = []
            pos_atual = pos_tesouro

            # montagem do caminho usando os predecessores de cada nó
            while pos_atual:
                caminho.append(pos_atual)
                pos_atual = pred.get(pos_atual)
            
            # retorna o caminho
            return caminho[::-1]

        if visited[x][y]:
            continue

        # marcando como visitado
        visited[x][y] = True 

        # explorando vizinhos
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy

            # verifica se o vizinho ta dentro da matriz
            if 0 <= nx < linhas and 0 <= ny < colunas and not visited[nx][ny]:

                if grid[x][y] == '#':
                    continue

                novo_custo = h((nx, ny))

                # Atualiza se o custo for menor
                if novo_custo < custo or (nx, ny) not in pred:
                    pred[(nx, ny)] = (x, y)  # Rastreia o caminho
                    heapq.heappush(queue, (novo_custo, (nx, ny)))

    return []

def busca_a_estrela(grid, pos_inicial, pos_tesouro):
    
    def h(x):
        return abs(pos_tesouro[0] - x[0]) + abs(pos_tesouro[1] - x[1])

    # dimensões
    linhas, colunas = len(grid), len(grid[0])
    
    # movimentos possíveis
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # fila com os nós que devem ser visitados
    # custo total, custo g e posição
    queue = [(h(pos_inicial), 0, pos_inicial)] # (prioridade, nó)

    # Dicionário para armazenar os menores custos G já encontrados
    g_score = {pos_inicial: 0}

    # matriz de visitados
    visited = [[False] * colunas for _ in range(linhas)] 
    
    # dicionário com predecessores de cada nó visitado
    pred = {}

    while queue:

        # extraindo o custo e o proximo nó
        custo_h, custo_g, (x, y) = heapq.heappop(queue)

        # print(f'({x}, {y})')
        # tesouro encontado
        if (x, y) == pos_tesouro:
            caminho = []
            pos_atual = pos_tesouro

            # montagem do caminho usando os predecessores de cada nó
            while pos_atual:
                caminho.append(pos_atual)
                pos_atual = pred.get(pos_atual)
            
            # retorna o caminho
            return caminho[::-1]

        if visited[x][y]:
            continue

        # marcando como visitado
        visited[x][y] = True 

        # explorando vizinhos
        for dx, dy in movimentos:
            nx, ny = x + dx, y + dy

            # verifica se o vizinho ta dentro da matriz
            if 0 <= nx < linhas and 0 <= ny < colunas and not visited[nx][ny]:

                if grid[x][y] == '#':
                    continue
    
                if grid[nx][ny] == '.':  # Célula vazia
                    step_cost = 1
                elif grid[nx][ny] == 'L':  # Lama
                    step_cost = 5
                elif grid[nx][ny] == 'T':  # Tesouro
                    step_cost = 0
                else:
                    continue

                novo_custo = custo_g + step_cost
                

                # Se o novo custo for melhor, atualiza
                if (nx, ny) not in g_score or novo_custo < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = novo_custo
                    pred[(nx, ny)] = (x, y)  # Rastreia o caminho

                    custo_total = novo_custo + h((nx, ny))
                    heapq.heappush(queue, (custo_total, novo_custo, (nx, ny)))

    return []

grid = [
    ['I', '#', '.', '#', 'L', 'L', 'T'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.'],
]
pos_inicial = (0, 0)
pos_tesouro = (0, 6)

print_mapa(grid)

caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
caminho_a_estrela = busca_a_estrela(grid, pos_inicial, pos_tesouro)

# caminho_bcu = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]
# caminho_gulosa = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (8, 6), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9)]
# caminho_a_estrela = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]

# print(caminho_bcu)
print_caminho(grid, caminho_bcu, "Custo uniforme")
print_caminho(grid, caminho_gulosa, "Gulosa")
print_caminho(grid, caminho_a_estrela, "A*")