temps_negative = [220, 230, 450, 789, -9999]
temps_string = [220, 230, 450, 789, -9999,"test", "test_str"]
#list comprehension
#new_temps = [temp/10 for temp in temps_negative]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps_negative]

print(new_temps)

def zero_instead(temps_str):
    return [temp if not isinstance(temp, str) else 0 for temp in temps_str]

print(zero_instead(temps_string))