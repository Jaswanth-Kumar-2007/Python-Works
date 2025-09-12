def max_depth(lst):
    """
     Return the maximum nesting depth of lists. A flat list
     (includinghas depth 1. If there are nested lists inside,
     the depth increase
    """
    i = 0
    while i < len(lst):
        if type(lst[i]) == int or type(lst[i]) == float:
            lst.pop(i)  
        else:
            i += 1   
        
    if not lst:
        return 1
    
    if type(lst[0]) == list or type(lst[0]) == set or type(lst[0]) == tuple :
        return 1 + max_depth(list(lst[0]))
    else:
        return 1

#Test Cases:
#print(max_depth([1,2,[3,[4]]]))
#print(max_depth([1, 2, 3]))
#print(max_depth([])) 