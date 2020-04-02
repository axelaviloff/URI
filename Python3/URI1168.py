n = int(input())
for i in range(n):
    led = 0
    nmbr = str(input())
    for j in range(len(nmbr)):
        if nmbr[j] == "1":
            led += 2
        elif nmbr[j] == "7":
            led += 3
        elif nmbr[j] == "4":
            led += 4
        elif nmbr[j] in ["2", "3", "5"]:
            led += 5
        elif nmbr[j] in ["6", "9", "0"]:
            led += 6
        else:
            led += 7
    print("{} leds".format(led))
