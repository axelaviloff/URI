N = int(input())
for i in range(N):
    n1, c1, n2, c2 = input().split()
    x, y = map(int, input().split())
    if (x+y) % 2 == 0:
        s = "PAR"
        if c1 == s:
            print(n1)
        else:
            print(n2)
    else:
        s = "IMPAR"
        if c1 == s:
            print(n1)
        else:
            print(n2)