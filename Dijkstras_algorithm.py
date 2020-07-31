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

    def __init__(self, input_graph_dict: dict):
        self.__user_graph = input_graph_dict
        self.__loader()

    def __loader(self):
        children_nodes = set()
        for node in self.__user_graph:
            if node not in self.__parents_dict:
                self.__parents_dict[node] = None
                self.__costs_dict[node] = float('inf')
                for child_node in self.__user_graph[node]:
                    children_nodes.add(child_node)
        start_node = list(self.__parents_dict.keys() - children_nodes)[0]
        self.__costs_dict[start_node] = 0
        for child_node in self.__user_graph[start_node]:
            self.__parents_dict[child_node] = start_node
            self.__costs_dict[child_node] = self.__user_graph[start_node][child_node]

    def __find_lowest_cost_node(self):
        lowest_cost = float('inf')
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

print(DijkstrasAlgorithm(example_graph).find_the_cheapest_route('start_point', 'finish_point'))
