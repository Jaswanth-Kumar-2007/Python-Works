def group_by_word_length(words):
    dic = {}
    for i in words:
        if len(i) not in dic:
            dic[len(i)] = [i]
        else:
            dic[len(i)].append(i)
    return dic

print(group_by_word_length(["hi","cat","dog","yes"]))