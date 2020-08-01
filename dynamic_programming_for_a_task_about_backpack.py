'''
===============================================================

    An example of using dinamic programming in solving a task about backpack.
    Main idea of dinamic programming is about the way from small tasks to big tasks.

    The task: We have some backpack with well known capasity and some things
    with well known cost and weight. So, what things should we put in our
    backpack to take the most costs value?

===============================================================
'''

things_cost_dict = {
    "tape_recorder": 3000,
    "laptop": 2000,
    "guitar": 1500,
    "picture": 2500
}
things_weight_dict = {
    "tape_recorder": 4,
    "laptop": 3,
    "guitar": 1,
    "picture": 2
}
backpack_capacity = 4
backpack = []
backpack_with_items = []
for items in range(len(things_cost_dict)):
    backpack.append([])
    backpack_with_items.append([])
    for cell in range(backpack_capacity):
        backpack[items].append([])
        backpack_with_items[items].append([])
        backpack[items][cell] = 0
        backpack_with_items[items][cell] = ['']

for num, item in enumerate(things_weight_dict):
    for current_capaticy in range(backpack_capacity):
        if (num == 0 and (current_capaticy+1) >= things_weight_dict[item]):
            backpack[num][current_capaticy] = things_cost_dict[item]
            backpack_with_items[num][current_capaticy] = [item]
        elif (num > 0):
            if (current_capaticy == 0):
                if ((current_capaticy+1) >= things_weight_dict[item]):
                    if (things_cost_dict[item] >= backpack[num - 1][current_capaticy]):
                        backpack[num][current_capaticy] = things_cost_dict[item]
                        backpack_with_items[num][current_capaticy] = [item]
                    else:
                        backpack[num][current_capaticy] = backpack[num - 1][current_capaticy]
                        backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][current_capaticy]
                else:
                    backpack[num][current_capaticy] = backpack[num - 1][current_capaticy]
                    backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][current_capaticy]
            else:
                if ((current_capaticy+1) >= things_weight_dict[item]):
                    if (things_cost_dict[item] + backpack[num - 1][current_capaticy + 1 - things_weight_dict[item]] >= backpack[num - 1][current_capaticy]):
                        backpack[num][current_capaticy] = things_cost_dict[item] + backpack[num - 1][current_capaticy + 1 - things_weight_dict[item]]
                        backpack_with_items[num][current_capaticy] = [item] + backpack_with_items[num - 1][current_capaticy + 1 - things_weight_dict[item]]
                    else:
                        backpack[num][current_capaticy] = backpack[num - 1][current_capaticy]
                        backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][current_capaticy]
                else:
                    backpack[num][current_capaticy] = backpack[num - 1][current_capaticy]
                    backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][current_capaticy]

print(backpack)
print(backpack_with_items)




