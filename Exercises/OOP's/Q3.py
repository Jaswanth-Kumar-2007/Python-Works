main_dir = {}

class Vehicle:
    def __init__(self,modelno,regno,manfdate,ownername,city,price):
        self.modelno = modelno
        self.regno = regno
        self.manfdate = manfdate
        self.ownername = ownername
        self.city = city
        self.price = price
        main_dir[self.modelno] = [modelno,regno,manfdate,ownername,city,price]

    def display(self):
        print(self.modelno,self.regno,self.manfdate,self.ownername,self.city,self.price)

    def count(self):
        print(len(main_dir))

a1 = Vehicle(1,2,3,4,5,6)
a2 = Vehicle(11,12,13,14,15,16)

a1.display()
a1.count()


