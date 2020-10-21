while True:
    a, b = map(int, input().split())
    if (a == b and b == 0):
        break
    else:
        soma = str(a+b)
        soma = soma.replace('0', '')
        print(soma)