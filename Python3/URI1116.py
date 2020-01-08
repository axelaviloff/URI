n = int(input())
for i in range(n):
    A, B = map(int, input().split())
    if B == 0:
        print("divisao impossivel")
    else:
        print("{:.1f}".format(A/B))
