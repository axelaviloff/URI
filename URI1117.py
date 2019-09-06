contador = 0
soma = 0
while contador != 2:
    nota = float(input())
    if not(0 <= nota <= 10):
        print("nota invalida")
    else:
        contador += 1
        soma += nota
print("media = {:.2f}".format(soma/2))