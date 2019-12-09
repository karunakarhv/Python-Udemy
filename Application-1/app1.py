import json
import os
import difflib
from difflib import get_close_matches

def check_closest_match(value):
    return get_close_matches(value, data.keys())[0]

if os.path.exists("data.json"):
    data = json.load(open("data.json"))
else:
    print("File does not exist")

while True:
    user_input = input("Enter the word: ")
    user_input = user_input.lower()
    if(user_input == "/end"):
        print("Closing the Dictionary")
        break 
    else:
        if user_input in data:
            meaning_list_index = 1
            if(type(data[user_input]) == list):
                for item in data[user_input]:
                    print("Meaning {}:{}".format(meaning_list_index, item))
                    meaning_list_index += 1
            else:
                print(data[user_input])
        elif user_input.title() in data:
            value_title = user_input.title()
            meaning_list_index = 1
            if(type(value_title) == list):
                for item in data[value_title]:
                    print("Meaning {}:{}".format(meaning_list_index, item))
                    meaning_list_index += 1
            else:
                print(data[value_title])
        elif user_input.upper() in data:
            value_upper = user_input.upper()
            meaning_list_index = 1
            if(type(value_upper) == list):
                for item in data[value_upper]:
                    print("Meaning {}:{}".format(meaning_list_index, item))
                    meaning_list_index += 1
            else:
                print(data[value_upper])
        else:
            close_match = check_closest_match(user_input)
            print(close_match)
            print("Did you mean %s"%(close_match))
            accept_value_not = input("If Yes please press Enter Y else Enter N:")
            accept_value_not = accept_value_not.upper()
            if(accept_value_not == 'Y'):
                meaning_list_index = 1
                if(type(data[close_match]) == list):
                    for item in data[close_match]:
                        print("Meaning {}:{}".format(meaning_list_index, item))
                        meaning_list_index += 1
                else:
                    print(data[close_match])
            elif(accept_value_not == 'N'):
                print("Item does not exist in dictionary.Please double check!!!")
            else:
                print("Did not understand your input.")

        
