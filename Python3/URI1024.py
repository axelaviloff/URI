n = int(input())

for i in range(n):
    word = list(input())
    for i in range(len(word)):
        if 65 <= ord(word[i]) <= 90 or 97 <= ord(word[i]) <= 122:
            word[i] = chr(ord(word[i])+3)
    word = word[::-1]
    for i in range(int(len(word)/2), len(word)):
            word[i] = chr(ord(word[i])-1)
    word = "".join(word)
    print(word)