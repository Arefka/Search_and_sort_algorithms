
'''
===============================================================

    We have a task of calculation the sum numbers value in strings array. 
    The best way is to calculate the sum in process of reading strings from array

===============================================================
'''

def calculation_the_sum(sentences_list: list) -> int:
    counter = 0
    for sentence in sentences_list:
        integer_value = 0
        for element in sentence:
            if element.isdigit():
                if integer_value == 0:
                    integer_value = int(element)
                    counter += integer_value
                else:
                    counter -= integer_value
                    counter += int(str(integer_value) + element)
                    integer_value = 0
            else:
                integer_value = 0
    return counter


################# example: #################
first_example = [['4kkt20', '51ll'], 75]
second_example = [['50kk10&4hello6tell'], 70]
third_example = [['7"3ke9bmt1', 'nt3mb', '09g3h'], 35]

print(first_example[1] == calculation_the_sum(first_example[0]))
print(second_example[1] == calculation_the_sum(second_example[0]))
print(third_example[1] == calculation_the_sum(third_example[0]))