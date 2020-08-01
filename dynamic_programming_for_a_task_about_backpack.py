'''
===============================================================

    An example of using dinamic programming in solving a task about backpack.
    Main idea of dinamic programming is about the way from small tasks to big tasks.

    The task: We have some backpack with well known capasity and some things
    with well known cost and weight. So, what things should we put in our
    backpack to take the most costs value?

===============================================================
'''

class BackpackTask:
    def __init__(self, things_cost: dict, things_weight: dict, backpack_capacity: int):
        self.__things_cost_dict = things_cost
        self.__things_weight_dict = things_weight
        self.__backpack_capacity = backpack_capacity

    def choose_items_for_backpack(self) -> []:
        backpack_with_costs = []
        backpack_with_items = []

        for items in range(len(self.__things_cost_dict)):
            backpack_with_costs.append([])
            backpack_with_items.append([])
            for cell in range(self.__backpack_capacity):
                backpack_with_costs[items].append([])
                backpack_with_items[items].append([])
                backpack_with_costs[items][cell] = 0
                backpack_with_items[items][cell] = ['']

        for num, item in enumerate(self.__things_weight_dict):
            for current_capaticy in range(self.__backpack_capacity):
                if (num == 0 and (current_capaticy + 1) >= self.__things_weight_dict[item]):
                    backpack_with_costs[num][current_capaticy] = self.__things_cost_dict[item]
                    backpack_with_items[num][current_capaticy] = [item]
                elif (num > 0):
                    if (current_capaticy == 0):
                        if ((current_capaticy + 1) >= self.__things_weight_dict[item]):
                            if (self.__things_cost_dict[item] >= backpack_with_costs[num - 1][current_capaticy]):
                                backpack_with_costs[num][current_capaticy] = self.__things_cost_dict[item]
                                backpack_with_items[num][current_capaticy] = [item]
                            else:
                                backpack_with_costs[num][current_capaticy] = backpack_with_costs[num - 1][
                                    current_capaticy]
                                backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][
                                    current_capaticy]
                        else:
                            backpack_with_costs[num][current_capaticy] = backpack_with_costs[num - 1][current_capaticy]
                            backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][current_capaticy]
                    else:
                        if ((current_capaticy + 1) >= self.__things_weight_dict[item]):
                            if (self.__things_cost_dict[item] + backpack_with_costs[num - 1][
                                current_capaticy + 1 - self.__things_weight_dict[item]] >= backpack_with_costs[num - 1][
                                current_capaticy]):
                                backpack_with_costs[num][current_capaticy] = self.__things_cost_dict[item] + \
                                                                             backpack_with_costs[num - 1][
                                                                                 current_capaticy + 1 -
                                                                                 self.__things_weight_dict[item]]
                                backpack_with_items[num][current_capaticy] = [item] + backpack_with_items[num - 1][
                                    current_capaticy + 1 - self.__things_weight_dict[item]]
                            else:
                                backpack_with_costs[num][current_capaticy] = backpack_with_costs[num - 1][
                                    current_capaticy]
                                backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][
                                    current_capaticy]
                        else:
                            backpack_with_costs[num][current_capaticy] = backpack_with_costs[num - 1][current_capaticy]
                            backpack_with_items[num][current_capaticy] = backpack_with_items[num - 1][current_capaticy]

        result_cost = backpack_with_costs[len(backpack_with_costs) - 1][::-len(backpack_with_costs) - 1][0]
        result_items = ','.join(backpack_with_items[len(backpack_with_items) - 1][::-len(backpack_with_items) - 1][0])

        return [result_cost, result_items]

################# example: #################
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

print(BackpackTask(things_cost_dict, things_weight_dict, backpack_capacity).choose_items_for_backpack())




