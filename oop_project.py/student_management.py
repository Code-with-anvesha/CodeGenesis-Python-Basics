
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def display(self):
        print(f" Student: {self.name} ({self.roll_no})")
        for subject, marks in self.marks.items():
            print(f" {subject}: {marks}")

    def new_method(self):
        return Student("Shubham", 102)


# Creating students 
s1 = Student("Anvesha", 101)
s2 = s1.new_method()  

s1.add_marks("Math", 95)
s1.add_marks("Science", 90)

s2.add_marks("Math", 85)
s2.add_marks("Science", 88)

s1.display()
s2.display()