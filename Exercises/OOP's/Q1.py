# Base Class
class Shape:
    def __init__(self,color,thickness):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass

# Triangle Class
class Triangle(Shape):
    def __init__(self,color,thickness,base,height,side1,side2,side3):
        super().__init__(color,thickness)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        print(0.5 * self.base * self.height)

    def perimeter(self):
        print(self.side1 + self.side2 + self.side3)


# Circle class
class Circle(Shape):
    def __init__(self, color, border_thickness, radius):
        super().__init__(color, border_thickness)
        self.radius = radius

    def area(self):
        print((22/7) * self.radius ** 2)

    def perimeter(self):
        print(2 * (22/7) * self.radius)


# Rectangle class
class Rectangle(Shape):
    def __init__(self, color, border_thickness, length, width):
        super().__init__(color, border_thickness)
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

    def perimeter(self):
        print(2 * (self.length + self.width))

rectangle1 = Rectangle("White",5,2,3)

rectangle1.area()
