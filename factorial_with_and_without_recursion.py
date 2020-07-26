'''
===============================================================

    The main idea of factorials algorithm with recursion is about splitting task to the base and recursion parts.

===============================================================
'''

def factorial_with_recursion(input_value: int) -> int:
    if input_value == 1:
        return 1
    else:
        return input_value * factorial_with_recursion(input_value - 1)

def factorial_without_recursion(input_value: int) -> int:
    output_value = 1
    for counter in range(2, input_value+1):
        output_value *= counter
    return output_value
