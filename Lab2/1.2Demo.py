import networkx as nx
import matplotlib.pyplot as plt

# 创建一个有向图
G = nx.DiGraph()

# 添加节点
G.add_node("A")
G.add_node("B")
G.add_node("C")

# 添加边
G.add_edge("A", "B")
G.add_edge("B", "C")

# 绘制图形
nx.draw(G, with_labels=True)
plt.show()
