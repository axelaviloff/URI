x = input().split()
A = float(x[0])
B = float(x[1])
C = float(x[2])
aux = 0
if C > B:
    aux = B
    B = C
    C = aux
if C > A:
    aux = A
    A = C
    C = aux
if B > A:
    aux = A
    A = B
    B = aux

if A >= B+C:
    print("NAO FORMA TRIANGULO")
else:
    if A ** 2 == B ** 2 + C ** 2:
        print("TRIANGULO RETANGULO")
    elif A ** 2 > B ** 2 + C ** 2:
        print("TRIANGULO OBTUSANGULO")
    elif A ** 2 < B ** 2 + C ** 2:
        print("TRIANGULO ACUTANGULO")
    if A == B and B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
