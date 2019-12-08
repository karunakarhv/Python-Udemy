# Sum of all floating string numbers.
list_strings_float = ['1.0', '1.0', '1.0']
def convert_and_sum(list_value):
    return sum([ float(i) for i in list_value])

print(convert_and_sum(list_strings_float))