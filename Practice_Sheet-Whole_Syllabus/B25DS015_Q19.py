def str_lst(word):
    res = []
    for i in word:
        res.append(i)
    return res


def group_anagram(words):
    res = {}
    for i in range(len(words)):
        res1 = []
        for j in range(len(words)):
            if sorted(str_lst(words[i])) == sorted(str_lst(words[j])):
                res1.append(words[j])
        res["".join(sorted(str_lst(words[i])))] = res1
    return res

print(group_anagram(["eat","tea","tan","ate","nat"]))
