## 1. Capitalize the first word
## 2. If the first word starts with (how, who, where, what) put a question mark at the end of the string.
## 3. If the first word starts other than point 2, put a full stop(.) at the end of the string.
## 4. Print the string appended when the user inputs
## 5. To end the program use /end

def syntaxChange(value):
    tuple_interrogatives = ("how","who","where", "what")
    capitalized = value.capitalize()
    if(value.startswith(tuple_interrogatives)):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

result_list = []

while True:
    user_input = input("Say Something to do: ")
    if(user_input == "/end"):
        break
    else:
        result_list.append(syntaxChange(user_input))

print("".join(result_list))