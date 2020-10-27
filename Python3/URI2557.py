while True:
    try:
        eq = input()
        eq = eq.replace("=", "+")
        eq = eq.split("+")

        if eq[0] == "R":
            print(int(eq[2]) - int(eq[1]))
        elif eq[1] == "L":
            print(int(eq[2]) - int(eq[0]))
        elif eq[2] == "J":
            print(int(eq[0]) + int(eq[1]))
    except EOFError:
        break