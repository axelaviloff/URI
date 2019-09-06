cpares = 0
for i in range(1, 6):
    x = int(input())
    if x % 2 == 0:
        cpares += 1
print("{} valores pares".format(cpares))
