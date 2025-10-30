class Time:

    def __init__(self, h, m):
        total_m = h * 60 + m
        self.h = total_m // 60
        self.m = total_m % 60

    def __add__(self, rem):
        return Time(self.h + rem.h, self.m + rem.m)

    def __sub__(self, rem):
        t1 = self.h * 60 + self.m
        t2 = rem.h * 60 + rem.m
        diff = max(0, t1 - t2)
        return Time(0, diff)

    def display(self):
        return f"{self.h:02d}:{self.m:02d}"

t1 = Time(2,45)
t2 = Time(1,30)
print((t1 + t2).display()) 
print((t1 - t2).display()) 
print(Time(0,90).display()) 
