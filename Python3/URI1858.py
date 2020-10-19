N = int(input())
x = list(map(int, input().split()))
menor = min(x)
print(x.index(menor) + 1)