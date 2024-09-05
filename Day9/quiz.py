starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary['c']= 7
final_dictionary= starting_dictionary
print(final_dictionary)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict['c']= [1, 2, 3]

for key in dict:
    dict[key] += 1
print(dict[1])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

# "Steak"

print(order['main'][2][0])



