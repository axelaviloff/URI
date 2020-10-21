n = int(input())
for i in range(n):
    soma = 0
    hame, kame = input().split("k")
    soma += (hame.count("a") * kame.count("a"))
    print("k" + "a" * soma)