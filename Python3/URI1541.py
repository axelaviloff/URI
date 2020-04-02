from math import sqrt
while True:
    vet = input().split()
    A = int(vet[0])
    if A == 0:
        break
    B = int(vet[1])
    C = int(vet[2])
    resultado = int(sqrt((A*B)/(C/100)))
    print(resultado)