N = int(input())
inside = 0
outside = 0
if N < 10000:
    for i in range(0, N):
        X = int(input())
        if -10**7 < X < 10**7:
           if 10 <= X <= 20:
                inside += 1
           else:
                outside += 1

print("{} in".format(inside))
print("{} out".format(outside))