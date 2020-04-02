A = E = H = M = X = 0
N = int(input())
for i in range(N):
    nome, tipo = input().split()
    tipo = tipo.upper()
    if tipo == "A":
        A += 1
    elif tipo == "E":
        E += 1
    elif tipo == "H":
        H += 1
    elif tipo == "M":
        M += 1
    else:
        X += 1

print("{} Hobbit(s)".format(X))
print("{} Humano(s)".format(H))
print("{} Elfo(s)".format(E))
print("{} Anao(s)".format(A))
print("{} Mago(s)".format(M))
