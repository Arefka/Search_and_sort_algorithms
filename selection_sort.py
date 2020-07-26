'''
===============================================================

    Algorithmic complexity = O(n^2).

===============================================================
'''

def selection_sort(input_array: list):
    for i in range(1, len(input_array)):
        current_value = input_array[i]
        current_index = i
        while (current_index > 0 and current_value < input_array[current_index - 1]):
            input_array[current_index] = input_array[current_index - 1]
            current_index -= 1
        input_array[current_index] = current_value
