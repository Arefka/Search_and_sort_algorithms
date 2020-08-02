'''
===============================================================

    The task is about searching the maximum sequence of elements of monotonically increasing sequence.

===============================================================
'''

some_example_sequence = [1, 5, 2, 7, 8, 4, 6]

class MonotonicallyIncreadingSequence:
    def __init__(self, input_numerable_list: list):
        self.__numerable_list = input_numerable_list

    def __two_adjacent_elements_estimate(self):
        # TO DO
        # estimate two left elements and add result to the list
        return []

    def search_the_maximum_sequence(self):
        # we should split the input sequence to the list of monotonically increasing sequences
        maximum_monotonically_increasing_sequence = []
        while self.__numerable_list:
            current_monotonically_increasing_sequence = self.search_the_maximum_sequence()
            if len(maximum_monotonically_increasing_sequence) > len(current_monotonically_increasing_sequence):
                maximum_monotonically_increasing_sequence = current_monotonically_increasing_sequence
        return maximum_monotonically_increasing_sequence

