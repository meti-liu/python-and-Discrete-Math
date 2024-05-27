import networkx as nx
import  matplotlib.pyplot as plt


def Drawgragh(E):
    G = nx.Graph()
    G.add_edges_from(E)
    pos = nx.spring_layout(G)
    options = \
    {
        "font_size": 36,
        "node_size": 3000,
        "node_color": "red",
        "edge_color": "blue",
        "linewidths": 5,
        "font_color": "white",
        "width": 5,
    }
    plt.figure(figsize=(8, 6))
    plt.title("Undirected Graph")
    nx.draw_networkx(G, pos, **options)


def DrawDigragh(E):
    G = nx.DiGraph()
    G.add_edges_from(E)
    pos = nx.spring_layout(G)
    options = \
        {
            "font_size": 36,
            "node_size": 3000,
            "node_color": "red",
            "edge_color": "blue",
            "linewidths": 5,
            "font_color": "white",
            "width": 5,
            "with_labels": True,
            "arrows": True,
            "arrowstyle": '-|>',
        }
    plt.figure(figsize=(8, 6))
    plt.title("Directed Graph")
    nx.draw_networkx(G, pos, **options)



V1={'a','b','c','d','e','f'}
E1={('a','b'),('a','f'),('b','c'),('b','e'),('b','f'),('c','d'),('c','e'),('c','f'),('f','e')}
V2={'a','b','c','d','e','f'}
E2={('a', 'b'), ('a', 'c'), ('a', 'e'), ('b', 'd'), ('c', 'b'), ('d', 'c'), ('d', 'e'), ('e', 'a'), ('e', 'd')}
Drawgragh(E1)
DrawDigragh(E2)
plt.show()