import networkx as nx
import matplotlib.pyplot as plt

with open("input25.txt") as my_file:
    # First read the file and create the graph
    G = nx.Graph()
    for line in my_file.readlines():
        component1 = line.split(':')[0].strip()
        component_list = line.split(':')[1].strip().split(' ')
        G.add_node(component1)
        for component2 in component_list:
            G.add_node(component2)
            G.add_edge(component1, component2)
            #G.add_edge(component2, component1)

    # use networkx magic to process the graph, find and remove the edges
    print(G)
    edges_to_remove = nx.minimum_edge_cut(G)
    print(edges_to_remove)
    G.remove_edges_from(edges_to_remove)
    c1, c2 = nx.connected_components(G)

    # print answer and draw graph
    print(len(c1), len(c2), len(c1) * len(c2))
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
