# List Comprehension

"""
b = [(x,x**2,x**3) for x in range(20)]
c = [int(x) for x in ['10','20','30']]
d = [n for n in range(10,30)  if n%2 == 0]
e = [(i,j,k) for i in [1,2,3] for j in [3,4,5] for k in [5,6,7] if i != j and j != k and k != i]
f = [[1,3,5],[1,3,6],[1,3,7],[1,4,5]]
h = [n for ele in f for n in ele]
print(h)
"""

# Q1

res1 = [x for x in range(10,50) if x % 3 == 0 and x % 5 == 0]

# Q2

String = "Honesty is Best Policy"
res2 = " ".join([x.upper()  for x in String.split()])
#print(res2)

# Q3

lst = [(2,3,4),(),(3,4,),(0,)]
res3 = [x for x in lst if len(x) != 0]
#print(res3)


# Set Comprehension

"""
b = {(x,x**2,x**3) for x in range(10)}
c = {int(x) for x in ['10','20','30']}
d = {n for n in range(10,30)  if n%2 == 0}
e = {(i,j,k) for i in [1,2,3] for j in [3,4,5] for k in [5,6,7] if i != j and j != k and k != i}
f = {(1,3,5),(1,3,6),(1,3,7),(1,4,5)}
h = {n for ele in f for n in ele}
print(h)
"""

# Q1

st = {2,3,16,24,26,28,32,36,39,41,43,52}
res1 = {x for x in st if x not in range(20,40)}
#print(res1)

# Q2

res2 = {x**2 for x in range(5,11)}
#print(res2)

# Q3

#Requires Random Function


    
# Dictinary Comprehension"

"""
d = {"a":1,"b":2,"c":3,"d":4}
d1 = {k:v**3 for (k,v) in d.items()}
d2 = {k:v**3 for (k,v) in d.items() if v>3}
d3 = {k:("Even" if v%2 == 0 else "Odd") for (k,v) in d.items()}
print(d3)
"""

Emp = {
    "A101":{"name":"Ashish","age":30,"salary":21000},
    "B102":{"name":"Dinesh","age":25,"salary":12200},
    "C103":{"name":"Ramesh","age":28,"salary":110000}
    }

# Q1

res1 = {w:y  for w,y in Emp.items()  if y["age"] > 26}
#print(res1)

# Q2

res2 = {w:y for w,y in Emp.items() if y["name"][0:1] == "A"}
#print(res2)
