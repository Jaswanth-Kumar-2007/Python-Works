class Time:
    def __init__(h,m):
        self.h = h
        self.m = m
        if self.m > 30:
            self.p = self.h*3600+(60-self.m)*60
            return self.p
        else:
            self.p = self.h*3600+self.m*60
            return self.p

    def display(self):
        r = self.p//3600
        s = self.p%3600
        return f"{r}:{s}"

t1 = Time(2,45)
t2 = Time(1,30)
(t1 + t2).display()
(t1 - t2).display()
