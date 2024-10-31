import heapq
import networkx as nx

def dijkstra(graph: nx.Graph, start):
    distances = { node: float('inf') for node in graph.nodes }
    prev_nodes = { node: None for node in graph.nodes }
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        curr_dist, curr_node = heapq.heappop(min_heap)

        for neighbour in graph.neighbors(curr_node):
            weight = graph[curr_node][neighbour]['weight']
            distance = curr_dist + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                prev_nodes[neighbour] = curr_node
                heapq.heappush(min_heap, (distance, neighbour))

    return distances, prev_nodes

def reconstruct_path(prev_nodes, start, end):
    path = []
    curr_node = end
    while curr_node != start:
        if curr_node is None:
            return None # Шлях не існує
        path.append(curr_node)
        curr_node = prev_nodes[curr_node]
    path.append(start)
    path.reverse()
    return path

def main():
    # Створення графа з вагами (той самий граф)
    G = nx.Graph()

    # Додавання вершин (райони міста)
    nodes = ['A', 'B', 'C', 'D', 'E']
    G.add_nodes_from(nodes)

    # Додавання ребер з вагами
    edges = [
        ('A', 'B', 2),
        ('A', 'C', 5),
        ('B', 'C', 1),
        ('C', 'D', 2),
        ('D', 'E', 3),
        ('E', 'A', 4)
    ]
    G.add_weighted_edges_from(edges)

    # Знаходження найкоротших шляхів від кожної вершини до всіх інших
    all_shortest_paths = {}
    for source in G.nodes:
        distances, prev_nodes = dijkstra(G, source)
        paths = {}
        for target in G.nodes:
            if source != target:
                path = reconstruct_path(prev_nodes, source, target)
                paths[target] = (distances[target], path)
        all_shortest_paths[source] = paths

    # Виводимо результати
    for source in all_shortest_paths:
        print(f"\nНайкоротші шляхи від вершини {source}: ")
        for target in all_shortest_paths[source]:
            dist, path = all_shortest_paths[source][target]
            print(f" - До вершини {target}: шлях {path}, довжина {dist}")

if __name__ == '__main__':
    main()