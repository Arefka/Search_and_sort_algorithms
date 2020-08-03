'''
===============================================================

    Two ways of solving the task of search duplicate in numbers array:
    Algorithmic complexity of brute force way = O(n^2).
    Algorithmic complexity of way with items check = O(n).

===============================================================
'''
class SearchingDuplicates:
    def __init__(self, input_array:list):
        self.__user_list = input_array

    def brute_force_way(self) -> list:
        result_list = []
        for i in range(len(self.__user_list)):
            for j in range(i + 1, len(self.__user_list)):
                if self.__user_list[i] == self.__user_list[j]:
                    result_list.append(self.__user_list[i])
        return result_list

    def way_with_items_check(self):
        result_list = []
        checking_items_set = set()
        for num, item in enumerate(self.__user_list):
            if item not in checking_items_set:
                checking_items_set.add(item)
            else:
                result_list.append(item)
        return result_list

################# example: #################

my_list = [5, 2, 6, 1, -3, 2, 6, 4]
implementation_example = SearchingDuplicates(my_list)
print(implementation_example.brute_force_way())
print(implementation_example.way_with_items_check())