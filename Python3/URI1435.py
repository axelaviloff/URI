while True:
    n = int(input())
    if n == 0:
        break
    for i in range(n):
        linha = ''
        for j in range(n):
            linha += str(i)+" "
        print(linha.strip())