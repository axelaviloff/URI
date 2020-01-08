i = 1
j = 7
jc = 7
while i < 10:
    j = jc
    for x in range(3):
        print("I={} J={}".format(i, j))
        j -= 1
    i += 2
    jc += 2