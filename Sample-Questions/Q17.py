class Time:
    def __init__(self,h,m):
        self.h = h
        self.m = m

    def __add__(self,other):
        self.hh = self.h + other.h
        self.mm = self.m + other.m
        if self.mm > 60:
            s = self.mm//60
            self.hh = self.hh + s
            self.mm = self.mm - s*60
            return Time(self.hh,self.mm)
        else:
            return Time(self.hh,self.mm)
    
    def __sub__(self,other):
        self.hh = self.h - other.h
        self.mm = max(self.m,other.m) - min(self.m,other.m)
        return Time(self.hh,self.mm)

    def display(self):
        return f"Hours : {self.h},Minutes : {self.m}"

t1 = Time(2,50)
t2 = Time(1,30)

t = t1 + t2
s = t1 - t2

print(s.display())
print(t.display())
