# Name , Course Code , Credit , Grade Attained

def grade_point_avg(lst):
    sum = 0
    for i in lst:
        sum = sum + (i[2]*i[3])
    return sum / len(lst)

ans = [("Programming","CSL100",4.5,9),("Physics","PHL101",4,9)]

print(grade_point_avg(ans))