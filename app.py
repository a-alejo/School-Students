from Student import Student
# Choices are: name, age, major, gpa, is_graduating_this_year

Student1 = Student("David", 21, 'English', 2.7, True)
Student2 = Student("Alexa", 19, 'Math', 3.1, False)
Student3 = Student("Sofia", 24, 'Science', 3.7, True)
Student4 = Student("Tom", 22, 'Art', 2.9, False)
Student_All = Student1, Student2, Student3, Student4


for x in Student_All:
    print(x.name, x.honor_roll())
