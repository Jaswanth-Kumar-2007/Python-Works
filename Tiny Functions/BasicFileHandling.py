#Basic File Handling

with open("jk.txt","w") as file:
    file.write("Hello Python\n")
    file.write("File handling easy with Python")
    print("File Written Successfully")
    
f = open("jk.txt","r")
content = f.read()
print(content)
    

with open("jk.txt","a") as file:
    file.write("\nHello This Explains File handling")

a = open("jk.txt","r")
p = a.read()
print(p)
a.close()




