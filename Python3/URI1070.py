x = int(input())
if x % 2 == 1:
    for i in range(0, 6):
        print(x)
        x = x+2

else:
    x = x+1
    for i in range(0, 6):
        print(x)
        x = x+2
