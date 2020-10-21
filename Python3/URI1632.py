T = int(input())

for i in range(T):
    s = 1
    password = input()
    for c in password:
        if c in "aAeEiIoOsS":
            s *= 3
        else:
            s *= 2
    print(s)
