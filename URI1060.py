p = 0
n = 0
for i in range(0, 6):
    number = int(input())
    if number > 0:
        p += 1
    else:
        n += 1
print("%d valores positivos" % p)
