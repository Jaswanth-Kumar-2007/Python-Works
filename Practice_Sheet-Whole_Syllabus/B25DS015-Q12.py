def word_frequency(sentence):
    res = {}
    if sentence == "":
        return res
    p = sentence.lower()
    for i in p.split(" "):
        count = 0
        for j in p.split(" "):
            if i == j:
                count += 1
        res[i] = count
    return res

print(word_frequency(" "))
        
