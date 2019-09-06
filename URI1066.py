cPar = 0
cImpar = 0
cPositivo = 0
cNegativo = 0

for i in range(1, 6):
    x = int(input())
    if x > 0:
        cPositivo += 1
    if x < 0:
        cNegativo += 1
    if x % 2 == 0:
        cPar += 1
    else:
        cImpar += 1

print("{} valor(es) par(es)".format(cPar))
print("{} valor(es) impar(es)".format(cImpar))
print("{} valor(es) positivo(s)".format(cPositivo))
print("{} valor(es) negativo(s)".format(cNegativo))
