def mean(mylist):
    if(type(mylist) == dict):
        the_mean = sum(mylist.values())/len(mylist)
    else:
        the_mean = sum(mylist)/len(mylist)
    return the_mean

student_grades = [9.1, 8.8, 7.7, 10, 10, 10]
student_grades_dic = {"Marry":9.1, "Karun":9.9}
print(mean(student_grades))