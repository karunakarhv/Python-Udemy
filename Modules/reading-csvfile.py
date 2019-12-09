import pandas
import os
import time

while True:
    if os.path.exists("temps-today.csv"):
        data = pandas.read_csv("temps-today.csv")
        print(data.mean())
    else:
        print("File does not exist")
    time.sleep(10)