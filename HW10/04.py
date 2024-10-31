import uuid

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def count_nodes(root: Node):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def build_tree_from_heap(heap):
    if not heap:
        return None
    
    nodes = [Node(val) for val in heap]

    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2

        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
        
    return nodes[0]

def dfs_path(root: Node):
    s = [root]
    traversal_order = []
    while s:
        node = s.pop()
        if node:
            traversal_order.append(node)
            s.append(node.right)
            s.append(node.left)
    return traversal_order

def bfs_path(node: Node):
    q = deque([root])
    traversal_order = []
    while q:
        node = q.popleft()
        if node:
            traversal_order.append(node)
            q.append(node.left)
            q.append(node.right)
    return traversal_order

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def hex_color_gradient(start_hex, end_hex, steps):
    start_rgb = tuple(int(start_hex[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_hex[i:i+2], 16) for i in (1, 3, 5))

    gradient = []
    for step in range(steps):
        interpolate_rgb = tuple(
            int(start_rgb[i] + (end_rgb[i] - start_rgb[i]) * step / (steps - 1))
            for i in range(3)
        )
        gradient.append('#{:02x}{:02x}{:02x}'.format(*interpolate_rgb))
    return gradient

def visualize_traversal(root: Node, get_traversal_tree_order):
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(graph, root, pos)

    # Set gradient colors
    nodes_count = count_nodes(root)
    gradient_colors = hex_color_gradient("#003366", "#66b3ff", nodes_count)

    traversal_order = get_traversal_tree_order(root)
    plt.figure(figsize=(10, 8))
    for step, node in enumerate(traversal_order):
        nx.set_node_attributes(graph, {n.id: gradient_colors[step] for n in traversal_order[:step+1]}, "color")

        # Draw graph
        colors = [graph.nodes[n]["color"] for n in graph.nodes]
        labels = nx.get_node_attributes(graph, 'label')
        nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
        plt.pause(1) # Pause to show each step
        plt.clf()
    plt.show()

# Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

heap_list = [0, 4, 1, 5, 10, 3]
root = build_tree_from_heap(heap_list)

# Відображення дерева
#draw_tree(root)
visualize_traversal(root, bfs_path)
visualize_traversal(root, dfs_path)
