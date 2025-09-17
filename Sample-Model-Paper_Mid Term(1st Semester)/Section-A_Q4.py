def password_generator(name,year,color):
    #Name Password Generator
    p1 =  name[0:1].upper() 
    #year Password Generator
    q = str(year)
    p2 = q[::-1]
    #color Password Generator
    p3 = color[0:2].upper() 
    return p1 + p2 + p3

print(password_generator("ravi",2007,"blue"))