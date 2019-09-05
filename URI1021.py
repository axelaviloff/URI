N = float(input())
N += 0.001
nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota5 = 0
nota2 = 0
moeda1r = 0
moeda50 = 0
moeda25 = 0
moeda10 = 0
moeda5 = 0
moeda1c = 0

if 0 <= N <= 1000000:
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
    while N >= 1:
        N -= 1
        moeda1r += 1
    while N >= 0.50:
        N -= 0.50
        moeda50 += 1
    while N >= 0.25:
        N -= 0.25
        moeda25 += 1
    while N >= 0.10:
        N -= 0.10
        moeda10 += 1
    while N >= 0.05:
        N -= 0.05
        moeda5 += 1
    while N >= 0.01:
        N -= 0.01
        moeda1c += 1

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(nota100))
print("{} nota(s) de R$ 50.00".format(nota50))
print("{} nota(s) de R$ 20.00".format(nota20))
print("{} nota(s) de R$ 10.00".format(nota10))
print("{} nota(s) de R$ 5.00".format(nota5))
print("{} nota(s) de R$ 2.00".format(nota2))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moeda1r))
print("{} moeda(s) de R$ 0.50".format(moeda50))
print("{} moeda(s) de R$ 0.25".format(moeda25))
print("{} moeda(s) de R$ 0.10".format(moeda10))
print("{} moeda(s) de R$ 0.05".format(moeda5))
print("{} moeda(s) de R$ 0.01".format(moeda1c))
