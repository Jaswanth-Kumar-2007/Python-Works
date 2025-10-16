# OOP Basics

## Class

A Class is Blueprint for creating Objects

```python
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print(f"{self.color} {self.brand}")
```

## Object

An Object is an instance of a Class - created using the class blueprint.

```python
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Blue")

car1.show()
car2.show()
```

Output :

```python
Red Toyota
Blue BMW
```

## Encapsulation

Encapsulation means binding data and functions into a single unit (class) and restricting direct access to some attributes

```python
class Account:
    def __init__(self,balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)
```

```python
class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self._grade = "A"         # protected
        self.__marks = marks      # private

    def show(self):
        print(f"Name: {self.name}, Marks: {self.__marks}")

student1 = Student("Jaswanth", 95)

print(student1.name)      # ✅ public: accessible
print(student1._grade)    # ⚠️ possible but not recommended (Protected)
print(student1.__marks)   # ❌ Error: private (hidden)

student1.show()           # ✅ works fine
```

## Inheritance

Inheritance means one class can use properties and methods of another class . It allows code reusability

```python
class Animal:
    def speak(self):
        print("Animal Speaks")

class Dog(Animal):
    def bark(self):
        print("Dog Barks")

dog1 = Dog()
dog1.speak()
dog1.bark()
```

```python
class Dog:
    def make_sound(self):
        print("Bark 🐕")

class Cat:
    def make_sound(self):
        print("Meow 🐈")

class Cow:
    def make_sound(self):
        print("Moo 🐄")

# Same function name - works differently
animals = [Dog(), Cat(), Cow()]

for a in animals:
    a.make_sound()
```

```python
Bark
Meow
Moo
```

## Polymorphism

Polymorphism means same function name , different behavior depending on the object

```python
class Bird:
    def sound(self):
        print("Chirp")

class Dog:
    def sound(self):
        print("Bark")

for animal in (Bird(),Dog()):
    animal.sound()
```

## Abstraction

Abstraction means showing only the essential features and hiding the background details.

### In python , it's often done using abstract classes (via abc module)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
```

### Difference b/w with or without Abstraction

```python
class Shape:
    def area(self):
        pass  # you can just leave this empty

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

circle = Circle(5)
print(circle.area())

shape = Shape()
shape.area()   # does nothing
```

```python
from abc import ABC, abstractmethod

class Shape(ABC):           # Abstract base class
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

circle = Circle(5)
print(circle.area())

shape = Shape()   # ❌ Error: can't create abstract class
```

---

## THANK YOU
