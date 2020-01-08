lista = []
p = 0
maior = float("-inf")
for i in range(0, 100):
    lista.append(int(input()))

for i in range(0, len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        p = i
print(maior)
print(p + 1)
