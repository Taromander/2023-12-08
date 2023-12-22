class Course:
    def __init__(self, course_code, course_name, credit_hours, mandatory, instructor, class_time):
        self.course_code = course_code      # 課程代碼
        self.course_name = course_name      # 課程名稱
        self.credit_hours = credit_hours    # 學分數
        self.mandatory = mandatory          # 必選修
        self.instructor = instructor        # 任課老師
        self.class_time = class_time        # 上課時間

c1 = Course("CS101", "Introduction to Computer Science", 3, "必修", "Dr. Smith", "Monday 10:10 AM - 12:00 AM")
c2 = Course("CS102", "Introduction to Computer Science", 1, "選修", "Dr. Jhon", "Tuesday 8:10 AM - 11:00 AM")

print("課程代碼:", c1.course_code)
print("課程名稱:", c1.course_name)
print("學分數:", c1.credit_hours)
print("必選修:", c1.mandatory)
print("任課老師:", c1.instructor)
print("上課時間:", c1.class_time)

print("\n課程代碼:", c2.course_code)
print("課程名稱:", c2.course_name)
print("學分數:", c2.credit_hours)
print("必選修:", c2.mandatory)
print("任課老師:", c2.instructor)
print("上課時間:", c2.class_time)