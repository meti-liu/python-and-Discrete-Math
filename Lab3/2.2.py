import networkx as nx
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # Windows系统可以使用SimHei
matplotlib.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
def drawGraph(G, title):
    pos = nx.spring_layout(G)
    options = {
        "with_labels": True,
        "node_size": 500,
        "node_color": "red",
        "edge_color": "blue",
        "linewidths": 1,
        "font_size": 10,
        "font_color": "white",
        "width": 2,
    }
    plt.figure(figsize=(8, 6))
    plt.title(title)
    nx.draw_networkx(G, pos, **options)
    plt.show()

V = {'a', 'b', 'c', 'd', 'e'}
E = {('b', 'c'), ('a', 'c'), ('a', 'b'), ('a', 'd'), ('a', 'e'), ('b', 'd'),
     ('c', 'd'), ('c', 'e'), ('b', 'e'), ('d', 'e')}

G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

# 显示原图
drawGraph(G, "原图")


# subgraph 测试用例
Vs = {'a', 'b', 'c'}
subG = G.subgraph(Vs)
drawGraph(subG, "['a', 'b', 'c']子图")
print('子图节点:', subG.nodes())
print('子图边:', subG.edges())

# induced_subgraph 测试用例
Vs = {'a', 'b', 'c'}
induced_subG = nx.induced_subgraph(G, Vs)
drawGraph(induced_subG, "['a', 'b', 'c']导出子图")
print('导出子图节点:', induced_subG.nodes())
print('导出子图边:', induced_subG.edges())

# edge_subgraph 测试用例
Es = {('a', 'd'), ('a', 'c'), ('b', 'd')}
edge_subG = G.edge_subgraph(Es)
drawGraph(edge_subG, "[('a', 'd'), ('a', 'c'), ('b', 'd')]边子图")
print('边子图节点:', edge_subG.nodes())
print('边子图边:', edge_subG.edges())
