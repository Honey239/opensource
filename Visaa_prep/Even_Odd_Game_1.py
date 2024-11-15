n = int(input())
g = list(map(int,str(n)))
sum_d = 0
for i in range(len(g)):
    sum_d += g[i]
if sum_d%2==0:
    print("Vignesh")
else:
    print("Charan")
