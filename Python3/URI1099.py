n = int(input())
for i in range(n):
    soma = 0
    a, b = map(int, input().split())
    if a > b:
        for i in range(b+1, a):
            if i % 2 == 1:
                soma += i
    else:
        for i in range(a+1, b):
            if i % 2 == 1:
                soma += i
    print(soma)
