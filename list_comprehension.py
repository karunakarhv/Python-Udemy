temps = [220, 230, 450, 789, -9999]
#list comprehension
#new_temps = [temp/10 for temp in temps]

new_temps = [temp / 10 for temp in temps if temp != -9999]

#Older way of doing it
""" new_temps = []
for temp in temps:
    if(temp != -9999):
        value = temp/10
        new_temps.append(value) """

print(new_temps)