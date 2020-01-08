somaD = somaG = somaA = 0
opc = True
while opc:
    a = int(input())
    if a == 1:
        somaA += 1
    if a == 2:
        somaG += 1
    if a == 3:
        somaD += 1
    if a == 4:
        opc = False
    else:
        continue
print("MUITO OBRIGADO")
print("Alcool: {}".format(somaA))
print("Gasolina: {}".format(somaG))
print("Diesel: {}".format(somaD))
