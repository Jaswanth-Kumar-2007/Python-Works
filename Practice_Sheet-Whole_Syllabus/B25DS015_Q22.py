class Temperature:
    def __init__(self,num):
        self.num = num

    def to_fahrenheit(self):
        return float(((self.num * 5 )/9)-32)

    @classmethod

    def from_fahrenheit(cls,temp):
        return cls((temp-32)*5/9)

    def display(self):
        return f"{round(self.num)} C / {round(self.to_fahrenheit(), 1)} F"


print(Temperature(25).to_fahrenheit())
print(Temperature.from_fahrenheit(98.6).display())
