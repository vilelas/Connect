from algorithm.kruskal import Graph
from utils.read_file import read_file
from utils.plot_graph import plot_graph

matriz = read_file(r"data\SH07.txt")

g = Graph(len(matriz))

# lista_arestas = []
# lista_pesos = []
# lista_vertice = [str(i)  for i in range(0, len(matriz))]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j > i:
            g.addEdge(i,j,round(float(matriz[i][j])))
            # lista_arestas.append((i, j))
            # lista_pesos.append(round(float(matriz[i][j])))
g.KruskalMST()

# plot_graph("grafo", lista_arestas, len(matriz), lista_pesos, lista_vertice)