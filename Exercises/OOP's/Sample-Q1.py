class A: 
    def __init__(self): 
        self.value = 5 
    def get_val(self): 
        return self.value * 2 
class B(A): 
    def __init__(self): 
        super().__init__() 
        self.value = 10 
obj = B() 
print(obj.get_val()) 

# Output - 20