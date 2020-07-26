import random

'''
===============================================================

    Algorithmic complexity = O(n*Log n).
    The "divide and conquer" strategy is used

===============================================================
'''

def quicksort(input_list: list) -> list:
    if len(input_list) <= 1:
        return input_list
    else:
        pivot_value = random.choice(input_list)
        lesser_values = []
        greater_values = []
        current_value = []

        for value in input_list:
            if value < pivot_value:
                lesser_values.append(value)
            elif value > pivot_value:
                greater_values.append(value)
            else:
                current_value.append(value)

        return quicksort(lesser_values) + current_value + quicksort(greater_values)

