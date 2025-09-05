def max_even_sum_len(num):
    #For a sequence 1, 2, ..., N, find the maximum length
    #of a contiguous subsequence that has an even sum.
    sum = 0
    p = 1
    while p != num+1:
        sum = sum + p
        p = p + 1
    while sum % 2 != 0:
        sum = sum - p+1
        p = p-1
    else:
        print(p-1)
    

#TestCases:
#max_even_sum_len(3)
#max_even_sum_len(5)
#max_even_sum_len(9)
        