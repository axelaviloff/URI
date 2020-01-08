hi, mi, hf, mf = map(int, input().split(" "))
dMinutos = 0
dHoras = 0

if hf > hi and mf > mi:
    dHoras = hf - hi
    dMinutos = mf - mi
elif hf == hi and mf > mi:
    dHoras = 0
    dMinutos = mf - mi
elif hf == hi and mf < mi:
    #01:05 #01:01
    dHoras = 23
    dMinutos = 60-(mi-mf)
elif hf > hi and mf < mi:
    dHoras = 0
    dMinutos = 60-(mi-mf)
elif hf > hi and mf == mi:
    dHoras = hf - hi
    dMinutos = 0
elif hf == hi and mf == mi:
    dHoras = 24
    dMinutos = 0
elif hf < hi and mf > mi:
    dHoras = 24-hi
    dMinutos = mf-mi
elif hf < hi and mf == mi:
    #09:10 até 08:10
    dhoras = 23
    dMinutos = 0
else:
    dHoras = 23-(hi-hf)
    dMinutos = 60-(mi-mf)

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(dHoras, dMinutos))
