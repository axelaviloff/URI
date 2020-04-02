n = int(input())
for i in range(n):
    txt = input().split()
    palavra1 = txt[0]
    palavra2 = txt[1]
    palavra_final = ""
    ctd = 0
    while ctd < len(palavra1) and ctd < len(palavra2):
        palavra_final += (palavra1[ctd] + palavra2[ctd])
        ctd += 1
    if len(palavra1) > len(palavra2):
        palavra_final += palavra1[ctd:]
    else:
        palavra_final += palavra2[ctd:]
    
    print(palavra_final)

