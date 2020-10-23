while True:
    h1,m1,h2,m2 = map(int, input().split())
    
    if (h1 == 0 and m1 == 0 and h2 == 0 and m2 == 0):
        break
    
    h = h2 - h1
    m = m2 - m1

    if (h > 0):
        if (m >= 0):
            print(h * 60 + m)
        else:
            print(h * 60 - abs(m))
    
    elif (h < 0):
        if (m >= 0):
            print((24 * 60) - abs(h) * 60 + m)
        else:
            print((24 * 60) - (abs(h) * 60) - abs(m))
    
    else:
        if (m == 0):
            print(0)
        elif (m > 0):
            print(m)
        else:
            print(24 * 60 - abs(m))