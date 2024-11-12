from funcoes_auxiliares import print_mapa
from funcoes_auxiliares import print_caminho

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
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

# caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)
# caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
# caminho_a_estrela = busca_a_estrela(grid, pos_inicial, pos_tesouro)

# caminho_bcu = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]
# caminho_gulosa = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (4, 7), (5, 7), (6, 7), (6, 6), (7, 6), (8, 6), (8, 7), (9, 7), (9, 8), (9, 9), (8, 9), (7, 9), (6, 9)]
# caminho_a_estrela = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7), (2, 7), (2, 8), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9)]

# print_caminho(grid, caminho_bcu, "Custo uniforme")
# print_caminho(grid, caminho_gulosa, "Gulosa")
# print_caminho(grid, caminho_a_estrela, "A*")