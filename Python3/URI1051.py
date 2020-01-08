valor = float(input())

if 0 < valor <= 2000:
    print("Isento")
elif 2000< valor <=3000:
    t = valor - 2000
    tx = t*0.08
    print("R$ %.2f" % tx)
elif 3000 < valor <= 4500:
    t1 = valor - 3000
    tx1 = 1000 * 0.08
    tx2 = t1*0.18
    print("R$ %.2f" % (tx1 + tx2))
else:
    t1 = valor - 3000
    tx1 = 1000 * 0.08
    t2 = valor - 4500
    tx2 = 1500 * 0.18
    tx = t2 * 0.28
    print("R$ %.2f" % (tx + tx1 + tx2))



