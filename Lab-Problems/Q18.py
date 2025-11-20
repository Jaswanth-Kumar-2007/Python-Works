def train_square_function(x,lr,epochs):
    for i in range(epochs):
        x = x - lr * ( 2*x)
    return abs(x)

print(train_square_function(10,0.0,5))
print(train_square_function(5,0.1,10))
