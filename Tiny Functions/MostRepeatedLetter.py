def mode(l):
    p = list(l)
    max_word = p[0]
    maxcount = 0
    for i in p:
        count = 0
        for j in p:
            if i == j:
                count += 1
            if count > maxcount:
                maxcount = count
                mode = i
    return mode

print(mode("pineapple"))
                
