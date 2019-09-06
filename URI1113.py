while True:
    A, B = map(int, input().split())
    if A > B:
        print("Decrescente")
    elif A < B:
        print("Crescente")
    else:
        break
