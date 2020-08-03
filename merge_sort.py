'''
===============================================================

    MergeSort is a classic example of the "divide and conquer" strategy.
    Algorithmic complexity = O(n*Log n).

===============================================================
'''

def merge_sort(input_array: list) -> list:
    # let's determine the base case:
    if len(input_array) <= 1:
        return input_array

    # Let's determine the recursion case:
    middle_of_array = int(len(input_array)/2)
    left_part = merge_sort(input_array[:middle_of_array])
    right_part = merge_sort(input_array[middle_of_array:])

    return sort_action(left_part, right_part, input_array.copy())

def sort_action(left_part: list, right_part: list, array_cory: list) -> list:
    left_point = 0
    right_point = 0

    while left_point < len(left_part) and right_point < len(right_part):
        if left_part[left_point] <= right_part[right_point]:
            array_cory[left_point+right_point] = left_part[left_point]
            left_point += 1
        else:
            array_cory[left_point+right_point] = right_part[right_point]
            right_point += 1

    for i in range(left_point, len(left_part)):
        array_cory[i + right_point] = left_part[i]
    for j in range(right_point, len(right_part)):
        array_cory[left_point + j] = right_part[j]

    return array_cory

################# example: #################

my_list = [5, 2, 6, 1, -3, 2, 4]
print(merge_sort(my_list))