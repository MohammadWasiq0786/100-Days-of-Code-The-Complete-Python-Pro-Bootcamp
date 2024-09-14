# import random
# import math

# def mutate(a_list):
#     b_list= []
#     new_item= 0
#     for item in a_list:
#         new_item= item*2
#         new_item += random.randint(1, 3)
#         new_item= math.add(new_item, item)

#     b_list.append(new_item)
#     print(b_list)

import random

def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item += item
        b_list.append(new_item)
        print(b_list)

a_list = [1, 2, 3, 4, 5]
mutate(a_list)