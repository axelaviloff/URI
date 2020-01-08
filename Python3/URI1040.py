notas = input()
A, B, C, D = notas.split(" ")
A = float(A)
B = float(B)
C = float(C)
D = float(D)
media = (A*2+B*3+C*4+D*1)/10
if media >= 7:
    print("Media: {:.1f}".format(media))
    print("Aluno aprovado.")
elif 5 <= media <= 6.9:
    print("Media: {:.1f}".format(media))
    print("Aluno em exame.")
    ne = float(input())
    print("Nota do exame: {:.1f}".format(ne))
    nm = (media + ne)/2
    if nm >= 5:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(nm))
    else:
        print("Aluno reprovado.")
        print("Media final {:.1f}".format(nm))
else:
    print("Media: {:.1f}".format(media))
    print("Aluno reprovado.")