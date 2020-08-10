'''
===============================================================

    RSelect used the "divide and conquer" strategy.
    Algorithmic complexity = O(n).

===============================================================
'''

import random

def r_select(input_list: list, item_position:int):

    if len(input_list) == 1:
        return input_list[0]

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

    if item_position >= len(lesser_values) and item_position <= (len(lesser_values) + len(current_value) - 1):
        return current_value[0]
    elif item_position < len(lesser_values):
        return r_select(lesser_values, item_position)
    else:
        return r_select(greater_values, item_position - len(lesser_values) - len(current_value))


################# example: #################

my_list = [5, 1, 8, 6, 1, -3, 2, 4]
print(r_select(my_list, 3))
