N = int(input())
A = N
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
nota1 = 0
if 0 < N < 1000000:
    while N >= 100:
        N -= 100
        nota100 += 1
    while N >= 50:
        N -= 50
        nota50 += 1
    while N >= 20:
        N -= 20
        nota20 += 1
    while N >= 10:
        N -= 10
        nota10 += 1
    while N >= 5:
        N -= 5
        nota5 += 1
    while N >= 2:
        N -= 2
        nota2 += 1
    while 0 < N < 2:
        N -= 1
        nota1 += 1

print(A)
print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota5))
print("{} nota(s) de R$ 2,00".format(nota2))
print("{} nota(s) de R$ 1,00".format(nota1))
