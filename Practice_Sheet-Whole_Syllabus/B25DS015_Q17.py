def spiral_order(matrix):
    res = []
    for i in matrix:
        for j in i:
            res.append(j)
    return res

print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))