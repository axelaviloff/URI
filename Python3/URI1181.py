l = int(input())
operation = str(input())
resultado = 0.0
matrix = []

for i in range(12):
    line = []
    for j in range(12):
        line.append(float(input()))
    matrix.append(line)



for line in matrix[l]:
    resultado += element

if operation == "S":
    print(resultado)
else:
    print(resultado/12)