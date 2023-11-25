class Person:
    def __init__(self, full_name, age, is_married):
        self.fullname = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'Full name: {self.fullname} age: {self.age} is married: {self.is_married}'


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super(Student, self).__init__(fullname, age, is_married)
        self.marks = marks
        self.marks = dict(self.marks)

    def average_estimation(self):
        sum_marks = sum(self.marks.values())
        len_marks = len(self.marks.values())
        return sum_marks // len_marks

    def introduce_myself(self):
        return f'Full name: {self.fullname} age: {self.age} is married: {self.is_married} ' \
               f'marks: {self.marks}'


class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super(Teacher, self).__init__(full_name, age, is_married)
        self.experience = experience

    base_salary = 30000

    def bonus(self):
        if self.experience > 3:
            bonus_salary = 30000 * 0.05
            salary = self.base_salary + (bonus_salary * (self.experience - 3))
            return round(salary)

    def introduce_myself(self):
        return f'Full name: {self.fullname} age: {self.age} is married: {self.is_married} now salary: {self.bonus()}'


teacher = Teacher('Imangazieva Baktygul', 25, 'Yes', 7)
print(teacher.introduce_myself())


def create_students():
    student1 = Student('Asykbekov Elbars', 19, 'No', {'math': 70, 'phisyck': 80, 'history': 50})
    student2 = Student('Borubaev Amantai', 20, 'No', {'math': 90, 'phisyck': 85, 'history': 89})
    student3 = Student('Nurdinova Selim', 15, 'No', {'math': 60, 'phisyck': 77, 'history': 62})
    list_students = [student1, student2, student3]
    return list_students


students = create_students()
for i in students:
    print(f'{i.introduce_myself()} average estimation: {i.average_estimation()}')
