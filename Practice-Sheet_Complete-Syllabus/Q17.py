class InputParser:
    def __init__(self,input):
        self.input = input

    def split(self,delimeter):
        self.res = self.input.split(f"{delimeter}")
        return self.res

    def map(self,dtype):
        return list(map(dtype,self.res))

p = InputParser("10,20,30")
print(p.split(','))
print(p.map(int))