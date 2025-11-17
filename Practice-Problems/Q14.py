class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self,name,age,rollno,mat,phy,chem):
        super().__init__(name,age)
        self.rollno = rollno
        self.mat = mat
        self.phy = phy
        self.chem = chem

    def display(self):
        print(f"Name : {self.name} , Age : {self.age} , Roll No. : {self.rollno} , Maths : {self.mat} , Physiscs : {self.phy} , Chemistry : {self.chem}")

b = Student("Jaswanth",18,2,30,40,50)
b.display()

