import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from collections import deque

def dfs_path(graph: nx.Graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()
    path = path + [start]
    visited.add(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            result = dfs_path(graph, neighbor, goal, path, visited)
            if result is not None:
                return result
    return None

def bfs_path(graph: nx.Graph, start, goal, path=None, visited=None):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph.neighbors(node):
                new_path = path + [neighbor]
                queue.append(new_path)
    return None

def main():
    # Створення графа (той самий граф, що й раніше)
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

    dfs_result = dfs_path(G, 'A', 'E')
    print(f"Шлях DFS з 'A' до 'E': {dfs_result}")

    bfs_result = bfs_path(G, 'A', 'E')
    print(f"Шлях BFS з 'A' до 'E': {bfs_result}")

    # Візуалізація графа з виділенням шляхів DFS і BFS
    pos = nx.spring_layout(G)

    # Малюємо всі ребра
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5, edge_color='gray')

    # Малюємо вершини
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='lightblue')

    # Малюємо мітки вершин
    nx.draw_networkx_labels(G, pos)

    # Виділяємо шлях DFS
    edge_list_dfs = list(zip(dfs_result, dfs_result[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_list_dfs, width=3, edge_color='red', label='DFS Path')

    # Виділяємо шлях BFS
    edge_list_bfs = list(zip(bfs_result, bfs_result[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=edge_list_bfs, width=3, edge_color='green', label='BFS Path')

    # Створення легенди з відповідними мітками та стилями
    edge_all_legend = mlines.Line2D([], [], color='gray', alpha=0.5, linewidth=1, label='Ребра графа')
    edge_dfs_legend = mlines.Line2D([], [], color='red', linewidth=3, label='Шлях DFS')
    edge_bfs_legend = mlines.Line2D([], [], color='green', linewidth=3, label='Шлях BFS')

    plt.legend(handles=[edge_all_legend, edge_dfs_legend, edge_bfs_legend], loc='upper right')
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()