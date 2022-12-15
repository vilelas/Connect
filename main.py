from algorithm.kruskal import Graph
from utils.read_file import read_file
from utils.plot_graph import plot_graph

# Lê a matriz a partir do arquivo
matrix = read_file(r"data\SH07.txt")

# Cria um objeto do tipo Graph
g = Graph(len(matrix))

# Inicializa listas para armazenar as arestas, pesos e vértices
edges = []
weights = []
vertices = [str(i) for i in range(len(matrix))]

# Adiciona as arestas ao grafo e às listas
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        # Adiciona apenas as arestas que estão na parte superior da matriz
        # (para evitar adicionar arestas duplicadas)
        if j > i:
            g.add_edge(i, j, round(float(matrix[i][j])))
            edges.append((i, j))
            weights.append(round(float(matrix[i][j])))

# Calcula a árvore geradora mínima
g.kruskal_mst()
g.view_mst()

# Plota o gráfico
plot_graph("grafo", edges, len(matrix), weights, vertices)