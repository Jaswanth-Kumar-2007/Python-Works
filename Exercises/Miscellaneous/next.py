gen = (i*i for i in range(15))

print(gen)

print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())
print(next(gen))