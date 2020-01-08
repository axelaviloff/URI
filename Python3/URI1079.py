n = int(input())
for i in range(0,n):
    A,B,C = map(float, input().split())
    media = (2*A+3*B+5*C)/10
    print("{:.1f}".format(media))