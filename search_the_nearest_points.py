'''
===============================================================

    Task about search the nearest points on Euclidean plane:
    Algorithmic complexity of brute force way = O(n^2).
    Algorithmic complexity of way with soft = O(n*log n).

===============================================================
'''

class SearchTheNearestPoints:
    def brute_force_way(self, points_array) -> dict:
        result = {
            'first_point': [],
            'second_point': [],
            'distance_value' : float('inf')
        }

        for i in range(len(points_array) - 1):
            for j in range(i+1, len(points_array)):
                current_distance = (points_array[i][0] - points_array[j][0])**2 + (points_array[i][1] - points_array[j][1])**2
                if result['distance_value'] > current_distance:
                    result['distance_value'] = current_distance
                    result['first_point'] = points_array[i]
                    result['second_point'] = points_array[j]
        return result

    def merge_sort_idea(self, input_list) -> dict:
        # let's determine the base case:
        sorted_input_list = self.__merge_sort(input_list)
        if len(sorted_input_list) < 4:
            return self.brute_force_way(input_list)

        # Let's determine the recursion case:
        else:
            middle_point = int(len(sorted_input_list) / 2)
            left_part = sorted_input_list[:middle_point]
            right_part = sorted_input_list[middle_point:]
            left_result = self.merge_sort_idea(left_part)
            right_result = self.merge_sort_idea(right_part)

            if left_result["distance_value"] > right_result["distance_value"]:
                result = right_result
            else:
                result = left_result

            result_list = []
            for i in range(len(sorted_input_list)):
                if sorted_input_list[middle_point - 1][0] - result["distance_value"] < input_list[i][0] < sorted_input_list[middle_point - 1][0] + result["distance_value"]:
                    result_list.append(input_list[i])

            result_list = self.__merge_sort(result_list)
            if len(result_list) == 1:
                return result
            else:
                another_result = self.brute_force_way(result_list)
                if result["distance_value"] > another_result["distance_value"]:
                    return another_result
                else:
                    return result

    def __merge_sort(self, input_array: list) -> list:
        # let's determine the base case:
        if len(input_array) <= 1:
            return input_array

        if len(input_array) == 2:
            if input_array[0][1] > input_array[1][1]:
                return [input_array[1], input_array[0]]
            else:
                return input_array

        # Let's determine the recursion case:
        middle_of_array = int(len(input_array) / 2)
        left_part = self.__merge_sort(input_array[:middle_of_array])
        right_part = self.__merge_sort(input_array[middle_of_array:])

        return self.__sort_action(left_part, right_part, input_array.copy())

    def __sort_action(self, left_part: list, right_part: list, array_cory: list) -> list:
        left_point = 0
        right_point = 0

        while left_point < len(left_part) and right_point < len(right_part):
            if left_part[left_point] <= right_part[right_point]:
                array_cory[left_point + right_point] = left_part[left_point]
                left_point += 1
            else:
                array_cory[left_point + right_point] = right_part[right_point]
                right_point += 1

        for i in range(left_point, len(left_part)):
            array_cory[i + right_point] = left_part[i]
        for j in range(right_point, len(right_part)):
            array_cory[left_point + j] = right_part[j]

        return array_cory

################# example: #################

some_points = [[4,3], [1, 5], [2, 3], [5, 9], [2, 2], [4, 5]]
example_implementation = SearchTheNearestPoints()
print(example_implementation.brute_force_way(some_points))
print(example_implementation.merge_sort_idea(some_points))
