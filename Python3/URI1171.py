n = int(input())
lista = []
numerosTestados = []
for i in range(n):
    lista.append(int(input()))
lista.sort()
for valor in lista:
    if valor not in numerosTestados:
        print("{} aparece {} vez(es)".format(valor, lista.count(valor)))
        numerosTestados.append(valor)
