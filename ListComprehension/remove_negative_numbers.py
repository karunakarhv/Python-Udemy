def only_positive_numbers(list_value):
    return [i for i in list_value if i > 0]

print(only_positive_numbers([-1, -2, -3, 4, 5, 6]))