import collections
'''
===============================================================

    In this task we want to know does the path exist from start_node to finish_node.

===============================================================
'''

def is_the_path_exist(input_graph: dict, start_node: int, finish_node: int) -> bool:
    visited_nodes_set = {start_node}
    nodes_queue = collections.deque([start_node])
    visited_nodes_set.add(start_node)
    while nodes_queue:
        current_node = nodes_queue.popleft()
        if current_node in input_graph:
            for neighbour in input_graph[current_node]:
                if neighbour not in visited_nodes_set:
                    visited_nodes_set.add(neighbour)
                    if neighbour == finish_node:
                        return True
                    nodes_queue.append(neighbour)
    return False


################# example: #################

example_graph = {0: [1, 2, 3], 1: [5, 6], 2: [4], 3: [4], 4: [7], 6: [7], 5:[8], 7: [8]}
example_result = is_the_path_exist(example_graph, 0, 8)
print(example_result)