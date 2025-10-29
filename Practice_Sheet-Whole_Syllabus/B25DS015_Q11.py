def build_profile(first,last,**kwargs):
    user_profile = {}
    user_profile["first name"] = first
    user_profile["last name"] = last
    for key,value in kwargs.items():
        user_profile[key] = value
    return user_profile

print(build_profile("Jane","Smith",age=30,city="New York"))