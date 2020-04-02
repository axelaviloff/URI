operation = str(input())
resultado = 0.0
matrix = []

for i in range(12):
    line = []
    for j in range(12):
        line.append(float(input()))
    matrix.append(line)


for i in range(12):
    for j in range(12):
        if (i > j and i + j <= 10 and j <= 4):
            resultado += matrix[i][j]


if operation == "S":
    print("{:.1f}".format(resultado))
else:
    print("{:.1f}".format(resultado/30))

