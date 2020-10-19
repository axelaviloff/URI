T = int(input())
for i in range(T):
    sheldon = False
    
    opc = input().split()

    if opc[0] == opc[1]:
        print("Caso #{}: De novo!".format(i+1))
        continue

    if opc[0] == "tesoura" and (opc[1] == "papel" or opc[1] == "lagarto"):
        sheldon = True
    
    if opc[0] == "papel" and (opc[1] == "pedra" or opc[1] == "Spock"):
        sheldon = True
    
    if opc[0] == "pedra" and (opc[1] == "lagarto" or opc[1] == "tesoura"):
        sheldon = True
    
    if opc[0] == "lagarto" and (opc[1] == "Spock" or opc[1] == "papel"):
        sheldon = True

    if opc[0] == "Spock" and (opc[1] == "tesoura" or opc[1] == "pedra"):
        sheldon = True
    


    if sheldon:
        print("Caso #{}: Bazinga!".format(i+1))
    else:
        print("Caso #{}: Raj trapaceou!".format(i+1))
