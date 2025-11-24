s = 45

def add():
    s = 5
    s += 10
    print(s)

add()
print(s)

# 15 , 45

global p
p = 20

def addi():
    p = 5
    p += 10
    return p

print(addi())
print(p)

# 15 , 20