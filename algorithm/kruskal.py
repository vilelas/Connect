class Graph:
    def __init__(self, num_vertices):
        # Número de vértices do grafo
        self.num_vertices = num_vertices
        self.result = [] 

        # Lista de arestas do grafo
        self.edges = []

    # Adiciona uma aresta ao grafo
    def add_edge(self, u, v, w):
        self.edges.append([u, v, w])

    # Encontra o conjunto de um elemento i
    # (utiliza técnica de compressão de caminho)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Realiza a união de dois conjuntos de x e y
    # (utiliza união por classificação)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Anexa a árvore de menor classificação sob a raiz da
        # árvore de alta classificação (união por classificação)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # Se as classificações são iguais, então faz com que um seja raiz
        # e incrementa sua classificação em um
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Constroi a MST utilizando o algoritmo de Kruskal
    def kruskal_mst(self):
        # Ordena as arestas pelo seu peso
        self.edges = sorted(self.edges, key=lambda edge: edge[2])

        # Inicializa a lista de pais e a lista de ranques com valores iniciais
        parent = list(range(self.num_vertices))
        rank = [0] * self.num_vertices

        e = 0  # Contador de arestas selecionadas
        i = 0  # Índice da aresta atual

        # Enquanto ainda não selecionamos todas as arestas
        while e < self.num_vertices - 1:
            # Pega a próxima aresta
            u, v, w = self.edges[i]
            i += 1

            # Encontra os pais de cada vértice da aresta
            x = self.find(parent, u)
            y = self.find(parent, v)

            # Se os pais forem diferentes, significa que a aresta não forma um ciclo
            # então adicionamos à MST e unimos os conjuntos de vértices
            if x != y:
                e += 1
                self.result.append([u, v, w])
                self.union(parent, rank, x, y)

    def view_mst(self):
        minimum_cost = 0
        print("A seguir estão as arestas da MST gerada:")
        for edge in self.result:
            u, v, weight = edge
            minimum_cost += weight
            print(f"{u} -- {v} ==  {weight}")
        print(f"Peso da árvore geradora mínima é: {minimum_cost}")
