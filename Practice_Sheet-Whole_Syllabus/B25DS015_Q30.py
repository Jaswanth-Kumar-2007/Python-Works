def rotate_matrix(matrix):
    res_transpose = []
    for i in range(len(matrix[0])):
        temp_transpose = []
        for j in range(len(matrix)):
            p = matrix[j][i]
            temp_transpose.insert(0,p)
        res_transpose.append(temp_transpose)
    return res_transpose

print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate_matrix([[1,2],[3,4]]))