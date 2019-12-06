temps = [220, 230, 450, 789]
#list comprehension
new_temps = [temp/10 for temp in temps]

#Older way of doing it
""" new_temps = []
for temp in temps:
    value = temp/10
    new_temps.append(value) """

print(new_temps)