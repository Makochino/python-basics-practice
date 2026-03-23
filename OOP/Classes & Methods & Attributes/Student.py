#First option with try/except
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):

        sum_of_grades = sum(self.grades)

        try:
            average_grade = round(sum_of_grades / len(self.grades))
        except ZeroDivisionError:
            print("Student must have grades to get average grade!!!")
        else:
            print(f"{self.name}'s average grade at school is {average_grade}")


student1 = Student("Susan", [])
student1.average()
#Second using if not self.grades to check whether list is empty
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        if not self.grades:
            print("Student must have grades to get average grade!!!")
            return None

        sum_of_grades = sum(self.grades)
        average_grade = round(sum_of_grades / len(self.grades))

        print(f"{self.name}'s average grade at school is {average_grade}")


student1 = Student("Susan", [])
student1.average()