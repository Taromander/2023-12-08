class Student:
    def __init__(stust,stu_name,stu_id,stu_age,stu_grade,stu_course_id):
        stust.stu_name = stu_name
        stust.stu_id = stu_id
        stust.stu_age = stu_age
        stust.stu_grade = stu_grade
        stust.stu_course_id = stu_course_id

    def __str__(stust):
        return f"Name:{stust.stu_name}\nStudent ID:{stust.stu_id}\nAge:{stust.stu_age}\nGrade:{stust.stu_grade}\nCourse ID:{stust.stu_course_id}\n"

class Person:
    def __init__(self,name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def __str__(self):
        return f"Name:{self.name}\nAge = {self.age}\nPosition:{self.position}\n"

p1 = Person("John",36,"Convinient-store-clerk")
print(p1)

p2 = Person("Sue",22,"Student")
print(p2.__dict__)    

p3 = Person("Bo-jun",69,"None")
print(p3)

stu_1 = Student("Yu-En Lin","4B1G095",19,"2nd","G0D17M01")
print(stu_1)
stu_2 = Student("Chi-Ling Bing","4B1G6969",46,"Graduated","None")
print(stu_2)
stu_3 = Student("Xu-kun Cai","4B1G1568",25,"4th","Basketball team")
print(stu_3)