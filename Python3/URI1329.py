while True:
    n = int(input())
    if n == 0:
        break
    entrada = input().split()
    c = k = 0
    for face in entrada:
        if face == "0":
            c += 1
        else:
            k += 1
    print("Mary won {} times and John won {} times".format(c, k))