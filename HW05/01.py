import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Додавання вершин (райони міста)
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')

# Додавання ребер (дороги між районами)
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('B', 'C')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
G.add_edge('E', 'A')

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500)
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")

print(f"\nСтупінь кожної вершини:")
for node, degree in G.degree():
    print(f"Вершина {node}: ступінь {degree}")