dia_inicial = int(input().split()[1])
hora = input().split(":")
hora_inicial, minuto_inicial, segundo_inicial = map(int, hora)
dia_final = int(input().split()[1])
hora = input().split(":")
hora_final, minuto_final, segundo_final = map(int, hora)

dias = dia_final - dia_inicial

horas = hora_final - hora_inicial

if horas < 0:
    horas += 24
    dias -= 1

minutos = minuto_final - minuto_inicial

if minutos < 0:
    minutos += 60
    horas -= 1

segundos = segundo_final - segundo_inicial

if segundos < 0:
    segundos += 60
    minutos -= 1

print("{} dia(s)".format(dias))
print("{} hora(s)".format(horas))
print("{} minuto(s)".format(minutos))
print("{} segundo(s)".format(segundos))

