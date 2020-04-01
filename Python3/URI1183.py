operation = str(input())
resultado = 0.0
matrix = []

for i in range(12):
    line = []
    for j in range(12):
        line.append(float(input()))
    matrix.append(line)


for i in range(len(matrix)):
    resultado += sum(matrix[i][i+1:])

if operation == "S":
    print("{:.1f}".format(resultado))
else:
    print("{:.1f}".format(resultado/66))


