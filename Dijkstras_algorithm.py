'''
===============================================================

    A searching task the cheapest route with Dijkstra's algorithm.

===============================================================
'''

class DijkstrasAlgorithm:
    __user_graph = {}
    __costs_dict = {}
    __parents_dict = {}
    __visited_nodes = []
    __infinity = float('inf')

    def __init__(self, input_graph_dict: dict, input_costs_dics: dict, input_parents_dict: dict):
        self.__user_graph = input_graph_dict
        self.__costs_dict = input_costs_dics
        self.__parents_dict = input_parents_dict

    def __find_lowest_cost_node(self):
        lowest_cost = self.__infinity
        lowest_cost_node = None
        for node in self.__costs_dict:
            cost = self.__costs_dict[node]
            if cost < lowest_cost and node not in self.__visited_nodes:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def find_the_cheapest_route(self, start_point, end_point):
        node = self.__find_lowest_cost_node()
        while node is not None:
            cost = self.__costs_dict[node]
            neighbors = self.__user_graph[node]
            for neighbor in neighbors:
                new_cost = cost + neighbors[neighbor]
                if self.__costs_dict[neighbor] > new_cost:
                    self.__costs_dict[neighbor] = new_cost
                    self.__parents_dict[neighbor] = node
            self.__visited_nodes.append(node)
            node = self.__find_lowest_cost_node()

        result_path = [end_point]
        parent_node = self.__parents_dict[end_point]
        while ((parent_node is not None) and (parent_node != start_point)):
            result_path.append(parent_node)
            parent_node = self.__parents_dict[parent_node]
        result_path.append(start_point)

        return self.__costs_dict[end_point], result_path[::-1]


################# example: #################
example_graph = {
    'start_point': {'A_point': 6, 'B_point': 2},
    'A_point': {'finish_point': 1},
    'B_point': {'A_point': 3, 'finish_point': 5},
    'finish_point': {}
}
costs_dict = {
    'start_point': 0,
    'A_point': 6,
    'B_point': 2,
    'finish_point': float('inf')
}
parents_dict = {
    'start_point': None,
    'A_point': 'start_point',
    'B_point': 'start_point',
    'finish_point': None
}

print(DijkstrasAlgorithm(example_graph, costs_dict, parents_dict).find_the_cheapest_route('start_point', 'finish_point'))