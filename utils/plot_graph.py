import igraph

def plot_graph(name, list_edge, qtd_vertex, list_weight, list_label):
    g = igraph.Graph(directed=False)
    g.add_vertices(qtd_vertex)
    g.add_edges(list_edge)
    g.es["weight"] = list_weight
    visual_style = {}
    visual_style["vertex_label"] = list_label
    visual_style["edge_label"] = list_weight
    igraph.plot(g, f"{name}.png", **visual_style)

