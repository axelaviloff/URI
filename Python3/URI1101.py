while True:
    string = ""
    soma = 0
    A,B = map(int, input().split())
    if A <= 0 or B <= 0:
        break
    elif A > B:
        for i in range(B, A+1):
            string += str(i)
            soma += i
        print("{} Sum={}".format(" ".join(string), soma))
    elif B > A:
        for i in range (A, B+1):
            string += str(i)
            soma += i
        print("{} Sum={}".format(" ".join(string), soma))
    else:
        string += str(A)
        soma = A+B
        print("{} Sum={}".format(" ".join(string), soma))
