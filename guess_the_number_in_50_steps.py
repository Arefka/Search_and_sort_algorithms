import random

'''
===============================================================
    
    We have a task of "guess the number in 50 steps". 
    We should find planned number in array of 1000000 numbers in 50 steps. 
    If we find it, we should return 0, else we think about finding number 
    and compare it with planned number. If planned number is bigger then
    our number, we should return 1, else we should return -1.
    
    We can use binary search as analogic, so 
    the "divide and conquer" strategy is used. Algorithmic complexity = O(Log n).

===============================================================
'''

def guess_number_search(guess: int) -> int:
    sequence = []
    for number in range(1, 1000001):
        sequence.append(number)
    lowest_position = 0
    highest_position = len(sequence) - 1

    counter = 1
    current_item = 0

    while lowest_position <= highest_position:
        middle_position = int((lowest_position + highest_position) / 2)
        current_item = sequence[middle_position]
        if current_item == guess:
            return 0
        elif current_item > guess:
            highest_position = middle_position - 1
        else:
            lowest_position = middle_position + 1
        if (counter < 50):
            counter += 1
        else:
            break

    print(counter)
    if (current_item < guess):
        return -1
    else:
        return 1

################# example: #################
guess_value = random.randint(0, 1000000)
print(guess_number_search(guess_value))