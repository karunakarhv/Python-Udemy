# Remove the strings in a list
# Retain only numbers 
# List Comprehension

def test_value(list_values):
    return [i for i in list_values if not isinstance(i, str)]

print(test_value([99, 100, "test value", 101, 102, "test" ]))