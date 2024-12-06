import sys

class NodeData:
    def __init__(self, visited, predecessor, distance):
        self.visited = visited
        self.predecessor = predecessor
        self.distance = distance

def find_minimum(node_data_dict):
    min_distance = sys.maxsize
    min_node = None
    for node, data in node_data_dict.items():
        if not data.visited and data.distance < min_distance:
            min_distance = data.distance
            min_node = node
    return min_node

def dijkstra(graph, start_node):
    node_data_dict = {node: NodeData(False, None, sys.maxsize) for node in graph}
    node_data_dict[start_node].distance = 0
    current_node = start_node

    while current_node is not None:
        node_data_dict[current_node].visited = True

        # Przechodzimy przez sąsiadów aktualnego węzła (tylko jednostronne krawędzie)
        for neighbor, weight in graph[current_node].items():
            if not node_data_dict[neighbor].visited:
                new_distance = node_data_dict[current_node].distance + weight
                if new_distance < node_data_dict[neighbor].distance:
                    node_data_dict[neighbor].distance = new_distance
                    node_data_dict[neighbor].predecessor = current_node

        # Szukamy następnego węzła do odwiedzenia (z najmniejszą odległością)
        current_node = find_minimum(node_data_dict)

    return node_data_dict

if __name__ == "__main__":
    # Graf skierowany w postaci słownika (jednostronne przejścia)
    graph = {
        'A': {'B': 2, 'D': 4},
        'B': {'C': 5, 'D': 1},
        'C': {'E':3},
        'D': {'C': 2},
        'E': {'B': 3}
    }

    start_node = 'A'
    result = dijkstra(graph, start_node)

    print("Node | Distance | Predecessor")
    for node, node_data in result.items():
        print(f"{node}   | {node_data.distance}       | {node_data.predecessor}")
