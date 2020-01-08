soma = 0
cp = 0
for i in range(1,7):
    x = float(input())
    if x > 0:
        cp += 1
        soma += x
print("{} valores positivos".format(cp))
print("{:.1f}".format(soma/cp))