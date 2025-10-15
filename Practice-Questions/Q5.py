def pangram(str):
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    res = []
    for i in str.lower():
        if i not in res:
            res.append(i)
    for j in res:
        if j in alphabets:
            alphabets.remove(j)
    if len(alphabets) == 0:
        return "This is a Pangram"
    else:
        return "This is not a Pangram"

alp = "The quick brown fox jumps over the lazy dog"

print(pangram(alp))