def evaluate(marks,divisor):
    try:
        if marks in range(0,100):
            res = marks/divisor
            return res
        else:
            return "ValueError"
    except ZeroDivisionError:
        return "ZeroDivisionError"


print(evaluate(50,2))
print(evaluate(-1,2))
print(evaluate(101,1))
print(evaluate(50,0))

    
