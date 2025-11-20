class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150 :
        return "InvalidAgeError"
    else:
        return "Valid Age"

print(check_age(0))
print(check_age(150))
print(check_age(-1))
print(check_age(151))