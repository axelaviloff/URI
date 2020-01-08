numeros = input()
A, B, C, D = numeros.split(" ")
A = int(A)
B = int(B)
C = int(C)
D = int(D)
somaCD = C+D
somaAB = A+B
if (B > C) and (D > A) and (somaCD > somaAB) and (A > 0) and (B > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
