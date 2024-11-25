import sys

class NodeData:
    def __init__(self, visited, predecessor, distance):
        self.visited = visited
        self.predecessor = predecessor
        self.distance = distance

def find_minimum(node_data_list):
    min_distance = sys.maxsize
    min_index = -1
    for i in range(len(node_data_list)):
        if not node_data_list[i].visited and node_data_list[i].distance < min_distance:
            min_distance = node_data_list[i].distance
            min_index = i
    return min_index

def dijkstra(matrix, start_node):
    node_data_list = []
    for i in range(len(matrix)):
        node_data_list.append(NodeData(False, -1, sys.maxsize))
    node_data_list[start_node].distance = 0
    current_node = start_node
    while current_node != -1:
        node_data_list[current_node].visited = True
        for i in range(len(matrix)):
            if matrix[current_node][i] > 0 and node_data_list[current_node].distance + matrix[current_node][i] < node_data_list[i].distance:
                node_data_list[i].distance = node_data_list[current_node].distance + matrix[current_node][i]
                node_data_list[i].predecessor = current_node
        current_node = find_minimum(node_data_list)
    return node_data_list

if __name__ == "__main__":
    #graf nieskierowany o nieujemnych wagach
    adjacency_matrix = [
        [0, 10, 0, 0, 0, 0],
        [10, 0, 5, 0, 0, 15],
        [0, 5, 0, 20, 0, 0],
        [0, 0, 20, 0, 10, 0],
        [0, 0, 0, 10, 0, 5],
        [0, 15, 0, 0, 5, 0]
    ]

    start_node = 0
    result = dijkstra(adjacency_matrix, start_node)

    print("Node | Distance | Predecessor")
    for i, node_data in enumerate(result):
        print(f"{i}    | {node_data.distance}       | {node_data.predecessor}")
