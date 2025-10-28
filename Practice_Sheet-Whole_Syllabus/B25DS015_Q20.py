def valid_sudoku_rows(board):
    lst = [1,2,3,4,5,6,7,8,9]
    for i in board:
        for j in i:
            if j != 0:
                if j not in lst:
                    return False
                else:
                    lst.remove(j)
    return True

print(valid_sudoku_rows([[5,3,3],[6,0,0],[0,9,8]]))
