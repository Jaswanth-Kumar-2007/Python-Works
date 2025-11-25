def uppercase(str):
    return [x for x in str.split(' ') if x[0:1].isupper() == True]

l = "I LOVE PYTHON and AI"
print(uppercase(l))