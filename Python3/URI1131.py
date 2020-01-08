opc = 1
somaI, somaG, cont, somaE = 0, 0, 0, 0
while opc == 1:
    cont += 1
    I, G = map(int, input().split())
    if I > G:
        somaI += 1
    elif G > I:
        somaG += 1
    else:
        somaE +=1
    opc = int(input("Novo grenal (1-sim 2-nao)\n"))

print("{} grenais".format(cont))
print("Inter:{}".format(somaI))
print("Gremio:{}".format(somaG))
print("Empates:{}".format(somaE))
if somaI > somaG:
    print("Inter venceu mais")
elif somaG > somaI:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
