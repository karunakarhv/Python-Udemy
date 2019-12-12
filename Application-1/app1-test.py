import json
import os
import difflib
from difflib import get_close_matches
import mysql.connector


def database_query(str):
    con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
    )
    cursor = con.cursor()
    # execute SQL query using execute() method.
    cursor.execute("SELECT * from Dictionary")

    # Get the fields name (only once!)
    field_name = [field[0] for field in cursor.description]

    # Fetch a single row using fetchone() method.
    values = cursor.fetchone()

    # create the row dictionary to be able to call row['login']
    row = dict(zip(field_name, values))

    # print the dictionary
    print(row)

    # print specific field
    #print(row['login'])

    # print all field
    for key in row:
        print(key," = ",row[key])

    #seek_cur.execute("SELECT Definition FROM Dictionary WHERE Expression = '{}'".format(str))
    #return seek_cur.fetchall()

""" def translate(w):
    w = w.lower()
    #data = database_query(w)
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
#output = translate(word)
output = database_query(word)
print(type(output))
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
"""
database_query("test")
