from math import sqrt

numeros = input()
A, B, C = numeros.split(" ")
A = float(A)
B = float(B)
C = float(C)
if A == 0:
    print("Impossivel calcular")
else:
    delta = (B ** 2) - 4 * A * C
    if delta >= 0:
        R1 = (-B + sqrt(delta)) / (2 * A)
        R2 = (-B - sqrt(delta)) / (2 * A)
        print("R1 = {:.5f}".format(R1))
        print("R2 = {:.5f}".format(R2))
    else:
        print("Impossivel calcular")
