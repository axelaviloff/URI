n = int(input())
totalCoelhos = 0
totalRatos = 0
totalSapos = 0
total = 0
for i in range(0, n):
    animal = input().split()
    if animal[1] == "C":
        totalCoelhos += int(animal[0])
        total += int(animal[0])
    elif animal[1] == "R":
        totalRatos += int(animal[0])
        total += int(animal[0])
    elif animal[1] == "S":
        totalSapos += int(animal[0])
        total += int(animal[0])
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(totalCoelhos))
print("Total de ratos: {}".format(totalRatos))
print("Total de sapos: {}".format(totalSapos))
print("Percentual de coelhos: {:.2f} %".format((totalCoelhos*100)/total))
print("Percentual de ratos: {:.2f} %".format((totalRatos*100)/total))
print("Percentual de sapos: {:.2f} %".format((totalSapos*100)/total))
