con = True
while con:
    cont, media, a = 0, 0, 3
    while cont < 2:
        X = float(input())
        if 0 <= X <= 10:
            cont += 1
            media += X
        else:
            print("nota invalida")
    print('media = %.2f' % (media / 2))
    while a != 1 and a != 2:
        a = int(input("novo calculo (1-sim 2-nao)\n"))
        if a == 1:
            continue
        elif a == 2:
            con = False
        else:
            a = int(input("novo calculo (1-sim 2-nao)\n"))
