'''
===============================================================

    A simple class with diverse methods of find missing elements.
    Just a little fun.

    Example of a truly array: [1, 5, 2, 3, 4]
    array_len = length of truly array. In this example N = 5

    So, if we have array_len = 5 and input array like this [1, 5, 3, 4]
    then we should find missing element "2"


===============================================================
'''

class CheckMissingElements:
    def __init__(self, array_len:int, input_list: list):
        self.__array_len = array_len
        self.__user_list = input_list

    def find_missing_element_first_way(self) -> list:
        etalon_set = set()
        user_set = set(self.__user_list)
        for i in range(1, self.__array_len + 1):
            etalon_set.add(i)
        return list(etalon_set - user_set)

    def find_missing_element_second_way(self) -> list:
        result_list = []
        for i in range(1, self.__array_len + 1):
            if i not in self.__user_list:
                result_list.append(i)
        return result_list

