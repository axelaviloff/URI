x = str(input())
x = x.split(" ")
A = float(x[0])
B = float(x[1])
C = float(x[2])
if A + B > C and A + C > B and C + B > A:
    print("Perimetro = {:.1f}".format(A+B+C))
else:
    print("Area = {:.1f}".format(((A+B)*C)/2))
