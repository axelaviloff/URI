while True:
    D, N = input().split()
    
    if (D == '0' and N == '0'):
        break
    
    N = list(N)
    
    for i in range(len(N)):
        if N[i] == D:
            N[i] = ""
    
    N = "".join(N)
    
    c = 0
    
    for i in range(len(N)):
        if N[i] == N[0]:
            c += 1
    
    if (len(N) == 0):
        print(0)
    
    elif c == len(N):
        print(int(N[0]))
    
    else:
        print(int(N))