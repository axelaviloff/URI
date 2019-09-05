numeros = input()
A, B, C = numeros.split(" ")
A = int(A)
B = int(B)
C = int(C)
AUX = 0

if C > B:
    AUX = B
    B = C
    C = AUX
if C > A:
    AUX = A
    A = C
    C = AUX
if B > A:
    AUX = A
    A = B
    B = AUX
print("{} eh o maior".format(A))
