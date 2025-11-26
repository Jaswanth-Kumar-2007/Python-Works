def anagram(s1,s2):
    res1,res2 = [],[]
    for i in s1:
        res1.append(i)
    for j in s2:
        res2.append(j)
    if sorted(res1) == sorted(res2):
        return True
    else:
        return False
    

s1 = "silent"
s2 = "listen"

print(anagram(s1,s2))
    