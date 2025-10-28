class Student:
    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        self.average = sum/len(self.marks)
        print(self.average)

    def grade(self):
        if self.average >= 75:
            self.grade = 'A'
        elif self.average >= 60:
            self.grade = 'B'
        else:
            self.grade = 'C'
        print(self.grade)

    def info(self):
        print(f"Name : {self.name} | Roll No. : {self.roll_number} | Average : {self.average} | Grade : {self.grade}")

s1 = Student("Alice",101,[80,70,90])
s1.average()
s1.grade()
s1.info()