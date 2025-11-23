class EvenIterator:
    def __init__(self,n):
        self.n = n
    
    def __next__(self,i):
        if i <= self.n:
            return True
        return False

    def __iter__(self):
        if self.n < 2:
            pass  
        else:
            i = 1
            while self.__next__(i):
                if i % 2 == 0:
                    yield i
                i += 1

print(list(EvenIterator(0)))
print(list(EvenIterator(1)))
print(list(EvenIterator(2)))
print(list(EvenIterator(3)))
print(list(EvenIterator(9)))
print(list(EvenIterator(-5)))

    





