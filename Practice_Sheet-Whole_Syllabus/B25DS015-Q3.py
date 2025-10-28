def count_vowels(s):
    count = 0
    for p in s.lower():
        if p == "a" or p == "e" or p == "i" or p == "o" or p == "u":
            count += 1
    return count
            
print(count_vowels("Apple"))
