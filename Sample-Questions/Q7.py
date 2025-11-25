s = {'Aman':56,'Riya':89,'Kabir':72,'Neha':89,'Tara':45}

t = max(s.values())
for k,v in s.items():
    if v == t:
        print(k,v)


