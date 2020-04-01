N = int(input())
vet = list(map(int, input().split()))

print("Menor valor: {}".format(min(vet)))
print("Posicao: {}".format(vet.index(min(vet))))