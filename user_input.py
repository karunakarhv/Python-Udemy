def password_controller(value):
    if(len(value) < 8):
        return False
    else:
        return True

user_input =  input("Enter the value of password\n")
print(password_controller(user_input))