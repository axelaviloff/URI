valores = input()
A, B = valores.split(" ")
A = int(A)
B = int(B)

if A == 1:
    print("Total: R$ {:.2f}".format(4 * B))
elif A == 2:
    print("Total: R$ {:.2f}".format(4.50 * B))
elif A == 3:
    print("Total: R$ {:.2f}".format(5 * B))
elif A == 4:
    print("Total: R$ {:.2f}".format(2 * B))
else:
    print("Total: R$ {:.2f}".format(1.50 * B))
