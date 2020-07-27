import collections
'''
===============================================================

    A searching task the shortest route for an unweighted graph.

===============================================================
'''

def calculate_the_shortest_route(input_graph: dict, start_node: int, finish_node: int) -> list:
    visited_nodes_dict = {}
    nodes_queue = collections.deque([start_node])
    visited_nodes_dict[start_node] = [start_node]
    while nodes_queue:
        current_node = nodes_queue.popleft()
        for neighbour in input_graph[current_node]:
            if neighbour not in visited_nodes_dict:
                visited_nodes_dict[neighbour] = [neighbour] + visited_nodes_dict[current_node]
                if neighbour == finish_node:
                    return visited_nodes_dict[neighbour][::-1]
                nodes_queue.append(neighbour)
    return []


################# example: #################

example_graph = {0: [1, 2], 1: [2, 4], 2: [3], 3: [], 4: [3]}
example_result = calculate_the_shortest_route(example_graph, 0, 3)
print(example_result)

