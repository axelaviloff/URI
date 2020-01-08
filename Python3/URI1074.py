N = int(input())

for i in range(0, N):
    x = int(input())
    if x > 0:
        if x % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")

    elif x < 0:
        if x % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    else:
        print("NULL")