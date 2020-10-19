cont = 0
soma = 0
while cont != 3:
    entrada = input()
    if entrada[0] == "c":
        print(soma)
        cont += 1
        soma = 0
    else:
        if entrada[0] == "*":
            soma += 4
        if entrada[1] == "*":
            soma += 2
        if entrada[2] == "*":
            soma += 1
    