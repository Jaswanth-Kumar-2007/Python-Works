def count_vowels(string):
    #counts the number of Vowels (a,e,i,o,u) in a string
    #Functions works case insensitive so all words converted into lower case
    string = string.lower()
    l = list(string)
    count = 0
    for p in l:
        if (p == "a" or p == "e" or p == "i" or p == "o" or p == "u"):
            count = count + 1
        pass
    return count

#TestCases:
#print(count_vowels("Hello World"))
#print(count_vowels("PYTHON"))
#print(count_vowels("Rhytm"))
#print(count_vowels("I enjoy writing clean,efficient code everyday"))