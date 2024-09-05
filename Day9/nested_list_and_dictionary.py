capitals= {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary

travel_log= {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

Print Lille
print(travel_log["France"][1])

nested_list= ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log= {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 12
        },
    "Germany":{
        "cities_visited": ["Stuttgart", "Hamburg", "Berlin"],
        "num_times_visited": 5
        },
}

print(travel_log["Germany"]["cities_visited"][2])
