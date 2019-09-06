valores = input()
read_valores = valores
valores = list(map(int, valores.split(" ")))
valores.sort()
for x in valores:
    print(x)
print("")
read_valores = list(map(int, read_valores.split(" ")))
for x in read_valores:
    print(x)