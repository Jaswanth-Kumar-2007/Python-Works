sentence = "AI2025 systems are very powerful"

words = sentence.split(" ")

ans = [len(word) for word in words if not any (ch.isdigit() for ch in word)]

print(ans)