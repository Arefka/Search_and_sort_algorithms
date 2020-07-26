'''
===============================================================

    Algorithmic complexity = O(Log n). (For sorted array only)

===============================================================
'''

def binary_search(list: list, necessary_item: int) -> bool:
    lowest_position = 0
    highest_position = len(list) - 1

    while lowest_position <= highest_position:
        middle_position = int((lowest_position + highest_position) / 2)
        current_item = list[middle_position]

        if current_item == necessary_item:
            return True
        elif current_item > necessary_item:
            highest_position = middle_position - 1
        else:
            lowest_position = middle_position + 1
    return False
