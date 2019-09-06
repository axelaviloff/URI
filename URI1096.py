j = 7
i = 1
while i < 10:
    j = 7
    for x in range(3):
        print("I={} J={}".format(i, j))
        j -= 1
    i = i + 2