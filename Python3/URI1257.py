numero_testes = int(input())
for i in range(numero_testes):
    numero_linhas = int(input())
    mat = []
    soma = 0

    #Preenchendo a matriz
    for j in range(numero_linhas):
        mat.append(input())
    #Somando posição na matriz e no alfabeto
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            soma += (ord(mat[i][j])-65 + (i + j))
    print(soma)

    


