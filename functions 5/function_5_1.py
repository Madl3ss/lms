start, *words, end = input().split()

for word in words:
    if start.lower() <= word.lower() <= end.lower():
        print(word, end=" ")