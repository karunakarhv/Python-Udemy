import time
import os

while True:
    if os.path.exists("vegetables.txt"):
        with open("vegetables.txt") as filehandle:
            print(filehandle.read())
    else:
            print("File does not exist")
    time.sleep(10)