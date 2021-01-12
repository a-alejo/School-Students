class Student:
    def __init__(self, name, age, major, gpa, is_graduating_this_year):
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.is_graduating_this_year = is_graduating_this_year
        # self.all = name, age, major, gpa, is_graduating_this_year

    def honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False
