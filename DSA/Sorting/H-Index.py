def HIndex(citations):
    citations.sort(reverse=True)  # sort descending
    h = 0
    for i, c in enumerate(citations, start=1):
        if c >= i:
            h = i
        else:
            break
    return h    
   
        
            

print(HIndex([3, 0, 5, 3, 0]))
print(HIndex([5, 1, 2, 4, 1]))   