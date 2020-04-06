n = int(input())

for i in range(n):
    txt = input().split()
    nm1 = txt[0]
    nm2 = txt[1]
    pos = (len(nm1) - len(nm2))
    if nm1[pos:] == nm2:
        print("encaixa")
    else:
        print("nao encaixa")
    