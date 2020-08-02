'''
===============================================================

    The task is about searching the maximum sequence of elements of monotonically increasing sequence.

    We should split the input sequence to the list of monotonically increasing sequences and
    return longest one. We can think about some sequence as monotonically increasing
    if its previous element is smaller then next.

===============================================================
'''

class MonotonicallyIncreadingSequence:
    def __init__(self, input_numerable_list: list):
        self.__numerable_list = input_numerable_list

    def __elements_estimate(self):
        locally_the_best_sequence = [self.__numerable_list.pop(0)]
        while self.__numerable_list and locally_the_best_sequence[-1:][0] <= self.__numerable_list[0]:
            locally_the_best_sequence.append(self.__numerable_list.pop(0))
        return locally_the_best_sequence

    def search_the_maximum_sequence(self):
        maximum_monotonically_increasing_sequence = []
        while self.__numerable_list:
            current_monotonically_increasing_sequence = self.__elements_estimate()
            if len(maximum_monotonically_increasing_sequence) < len(current_monotonically_increasing_sequence):
                maximum_monotonically_increasing_sequence = current_monotonically_increasing_sequence
        return maximum_monotonically_increasing_sequence

################# example: #################

example_sequence = [1, 5, 2, 7, 8, 4, 6]

print(MonotonicallyIncreadingSequence(example_sequence).search_the_maximum_sequence())