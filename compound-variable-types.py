student_grades = [9.1, 8.8, 7.7, 10, 10, 10]
print(student_grades)

print("Average of Student Grades is ", sum(student_grades)/len(student_grades))
print("Highest Element of List is ", max(student_grades))
print("Number of Occurrences of Number 10 in the list is ", student_grades.count(10))

print(list(range(1, 10, 1)))

students = ["Karun", "Adithi", "Anshu", student_grades]
print(students)

student_grades_dic = {"Marry":9.1, "Karun":9.9}

sumdic = sum(student_grades_dic.values())
length = len(student_grades_dic)

print("Average of Dictionary Values:",sumdic/length)

tuple_var = (1,2,3)
print(tuple_var)

