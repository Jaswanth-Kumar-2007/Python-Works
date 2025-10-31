class Stack:
    def __init__(self):
        self.lst = []

    def push(self,item):
        self.lst.append(item)
        return self.lst

    def pop(self):
        return self.lst.pop(-1)

    def size(self):
        return len(self.lst)

    def peek(self):
        return self.lst[len(self.lst)-1]

    def is_empty(self):
        if len(self.lst) != 0:
            return False
        else:
            return True

s = Stack()
print(s.push(10))
print(s.push(20))
print(s.push(30))
print(s.pop())
print(s.peek())
print(s.size())
print(s.is_empty())


