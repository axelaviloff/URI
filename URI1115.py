while True:
    A, B = map(int, input().split())
    if A == 0 or B == 0:
        break
    elif A > 0 and B > 0:
        print("primeiro")
    elif A > 0 and B < 0:
        print("quarto")
    elif A < 0 and B > 0:
        print("segundo")
    else:
        print("terceiro")