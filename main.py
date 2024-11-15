from funcoes_auxiliares import print_mapa
from funcoes_auxiliares import print_caminho

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    # definir os vizinhos
    vizinhos = []
    x = pos_inicial[1]
    y = pos_inicial[0]

    if y > 0: 
        vizinhos.append((y - 1, x))
    if y < len(grid) - 1:    
        vizinhos.append((y + 1, x))
    if x > 0: 
        vizinhos.append((y, x - 1))
    if x < len(grid) - 1:    
        vizinhos.append((y, x + 1))

    menor_custo = 999999
    # calcular o custo p cada vizinho
    for i in range(0, len(vizinhos)):
        x = vizinhos[i][1]
        y = vizinhos[i][0]
        
        match(grid[y][x]):
            case '.':
                if menor_custo > 1:
                    x_no_menor_custo = x
                    y_no_menor_custo = y
            case 'L':
                if menor_custo > 1:
                    x_no_menor_custo = x
                    y_no_menor_custo = y
                
            case '#':
                if menor_custo > 1:
                    x_no_menor_custo = x
                    y_no_menor_custo = y
            case 'T':
                    x_no_menor_custo = x
                    y_no_menor_custo = y
            case 'I':
                if menor_custo > 1:
                    x_no_menor_custo = x
                    y_no_menor_custo = y

            
    # repetir o processo p os nós vizinhos
    
    pass

def busca_gulosa(grid, pos_inicial, pos_tesouro):
    pass

def busca_a_estrela(grid, pos_inicial, pos_tesouro):
    pass

grid = [
    ['I', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '#', '#', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '#', '.', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '#', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '#', 'T'],
    ['.', '#', '#', '.', '#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '#', '.', '#', '.', '.', '.'],
]
pos_inicial = (0, 0)
pos_tesouro = (6, 9)

print_mapa(grid)

caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
# caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
# caminho_a_estrela = busca_a_estrela(grid, pos_inicial, pos_tesouro)

# caminho_bcu = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]
# caminho_gulosa = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (8, 6), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9)]
# caminho_a_estrela = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]

# print_caminho(grid, caminho_bcu, "Custo uniforme")
# print_caminho(grid, caminho_gulosa, "Gulosa")
# print_caminho(grid, caminho_a_estrela, "A*")