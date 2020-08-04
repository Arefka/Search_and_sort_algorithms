'''
===============================================================

    Task about search the nearest points on Euclidean plane:
    Algorithmic complexity of brute force way = O(n^2).

===============================================================
'''

class SearchTheNearestPoints:
    def __init__(self, input_point: list):
        self.__points = input_point

    def brute_force_way(self) -> list:
        min_distance = float('inf')
        result = []

        for i in range(len(self.__points)):
            for j in range(i+1, len(self.__points)):
                distance = (self.__points[i][0] - self.__points[j][0])^2 + (self.__points[i][1] - self.__points[j][1])^2
                if min_distance > distance:
                    min_distance = distance
                    result = [self.__points[i], self.__points[j]]
        return result

    #[To Do]
    #def way_with_soft(self):


################# example: #################

some_points = [[1,3], [1, 4], [2,3], [5, 9], [0, 2], [4, 5]]
example_implementation = SearchTheNearestPoints(some_points)
print(example_implementation.brute_force_way())