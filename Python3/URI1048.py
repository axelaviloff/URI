salario = float(input())
nSalario = 0
rGanho = 0
rPercentual = 0
if 0 < salario <= 400:
    rGanho = salario*0.15
    nSalario = (salario+rGanho)
    rPercentual = 15
elif 400.01 <= salario <= 800:
    rGanho = salario * 0.12
    nSalario = (salario + rGanho)
    rPercentual = 12
elif 800.01 <= salario <= 1200:
    rGanho = salario * 0.10
    nSalario = (salario + rGanho)
    rPercentual = 10
elif 1200.01 <= salario <= 2000:
    rGanho = salario * 0.07
    nSalario = (salario + rGanho)
    rPercentual = 7
else:
    rGanho = salario * 0.04
    nSalario = (salario + rGanho)
    rPercentual = 4

print("Novo salario: {:.2f}".format(nSalario))
print("Reajuste ganho: {:.2f}".format(rGanho))
print("Em percentual: {} %".format(rPercentual))
