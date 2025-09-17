def triangle_possible(a,b,c):
    if (a+b>c) and (b+c>a) and (c+a>b) :
        return "Triangle is Possible"
    else:
        return "Triangle is Not Possible"
    
print(triangle_possible(1,2,3))