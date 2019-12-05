str_input = input("Enter your name: ")
#message = "Hello %s!!!" % str_input
#Python 3.6
message = f"Hello {str_input}!!!"
print(message)

firstName = input("Enter your First name: ")
surName = input("Enter your Surname: ")
message = "Hello %s %s!!!" %(firstName, surName)
#Python 3.6
message = f"Hello {firstName} {surName}!!!"
print(message)
