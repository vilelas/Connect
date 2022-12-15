import igraph

# Função para plotar um grafo
def plot_graph(graph_name, edge_list, vertex_count, weight_list, label_list):
    # Cria um grafo não-direcionado
    g = igraph.Graph(directed=False)

    # Adiciona os vértices ao grafo
    g.add_vertices(vertex_count)

    # Adiciona as arestas ao grafo
    g.add_edges(edge_list)

    # Atribui os pesos às arestas
    g.es["weight"] = weight_list

    # Cria o estilo visual do grafo
    visual_style = {}

    # Atribui os rótulos aos vértices
    visual_style["vertex_label"] = label_list

    # Atribui os pesos às arestas
    visual_style["edge_label"] = weight_list

    # Plota o grafo em um arquivo de imagem
    igraph.plot(g, f"{graph_name}.png", **visual_style)


def plot_graph_mst(num_vertices, edge_list, edge_weight_list, vertex_label_list, ):
    # Cria um grafo
    g = igraph.Graph(directed=False)

    # Adiciona os vértices e as arestas ao grafo
    g.add_vertices(num_vertices)
    g.add_edges(edge_list)

    # Adiciona os pesos das arestas ao grafo
    g.es["weight"] = edge_weight_list

    # Define o estilo visual do grafo
    visual_style = {}

    # Define as etiquetas dos vértices
    visual_style["vertex_label"] = vertex_label_list

    # Define as etiquetas das arestas
    visual_style["edge_label"] = edge_weight_list

    # Destaca as arestas da MST
    visual_style["edge_color"] = ["black" if edge in mst else "grey" for edge in g.es]

    # Plota o grafo
    igraph.plot(g, f"{file_name}.png", **visual_style)
