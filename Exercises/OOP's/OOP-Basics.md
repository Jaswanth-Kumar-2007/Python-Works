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

## THANK YOU
