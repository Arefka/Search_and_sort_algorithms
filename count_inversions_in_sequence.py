'''
===============================================================
    Task of counting inversions in sequence:
    Algorithmic complexity of brute force way = O(n^2).
    Algorithmic complexity of way with soft = O(n*log n).
===============================================================
'''

class SearchInversions:
    def __init__(self, input_sequence: list):
        self.__sequence_list = input_sequence
        self.__result_list = []

    def brute_force_way(self) -> list:
        self.__result_list.clear()
        for i in range(len(self.__sequence_list)):
            for j in range(i+1, len(self.__sequence_list)):
                if i < j and self.__sequence_list[i] > self.__sequence_list[j]:
                    self.__result_list.append([self.__sequence_list[i], self.__sequence_list[j]])
        return self.__result_list

    def way_with_soft(self):
        self.__result_list.clear()
        self.__merge_sort_idea(self.__sequence_list)
        return self.__result_list

    def __merge_sort_idea(self, input_list):

        if len(input_list) <= 1:
            return input_list

        middle_of_list = int(len(input_list)/2)
        left_part = input_list[:middle_of_list]
        right_part = input_list[middle_of_list:]

        return self.__sort_action(left_part, right_part)

    def __sort_action(self, left_part: list, right_part: list) -> list:
        left_point = 0
        right_point = 0
        result = []

        while left_point < len(left_part) and right_point < len(right_part):
            if left_part[left_point] <= right_part[right_point]:
                result.append(left_part[left_point])
                left_part.remove(left_part[left_point])
            else:
                result.append(right_part[right_point])
                for i in range(len(left_part)):
                    self.__result_list.append([left_part[i], right_part[right_point]])
                right_part.remove(right_part[right_point])

        if len(left_part) == 0:
            result += right_part
        else:
            result += left_part

        return result

################# example: #################

example_list = [1, 3, 5, 2, 4, 6]
example_implementation = SearchInversions(example_list)
print(example_implementation.brute_force_way())
print(example_implementation.way_with_soft())