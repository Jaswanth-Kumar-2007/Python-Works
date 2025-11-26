def numbercheck(str):
    return [len(i) for i in str.split(" ") if all(j.isalpha() for j in i)]

print(numbercheck("AI2025 is a Important Concept but fails"))
