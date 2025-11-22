dic = {1:21,3:33,4:41,2:20}

# Sort Based on Value 
p = sorted(dic.items(),key= lambda x:x[1])

# Sort Based on Key
s = sorted(dic.items())

print(p,s)