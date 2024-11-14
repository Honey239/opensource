n = list(map(int,input().split(' ')))
min_planes = n[0]*100
if min_planes>=n[1]:
    planes = 0
else:
    planes = (n[1]-min_planes+99)//100
print(planes)
