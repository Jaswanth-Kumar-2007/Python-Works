def res(test_dict,sub_list):
    s = {}
    for key,value in test_dict.items():
        for j in sub_list:
            if j in value:
                s[key] = value
    for i,j in s.items():
        test_dict.pop(i)
    return test_dict


test_dict = {1:"Cinema is Love",2:"Music is Good"}
sub_list = ["Love","Great"]

print(res(test_dict,sub_list))