def freq_word(sen):
    sum = 0
    ans = []
    dic = {}
    for p in sen.split(" "):
        ans.append(p)
    for i in ans:
        count = 0
        for j in ans:
            if str(i) == str(j) :
                count += 1
        dic[str(i)] = int(count)
    for key,value in dic.items():
        sum += value
    return dic,sum

sen = "This is a carrot eaten by the a rabbit that died a long time ago"
    
print(freq_word(sen))