class Time:
    def __init__(self,hours,minutes):
        self.hours = hours
        self.minutes = minutes

    def __add__(self, other):
        self.hh = self.hours + other.hours
        self.mm = self.minutes + other.minutes
        if self.mm > 60:
            s = self.mm//60
            self.hh = self.hh+s
            self.mm = self.mm-s*60
        return Time(self.hh,self.mm)

    def display(self):
        return f"{self.hours}Hours:{self.minutes}Minutes"

s = Time(2,60)
p = Time(3,20)
q = Time(10,23)
t = s+p+q
print(t.display())