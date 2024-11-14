n = list(map(int,input().split(' ')))
x,y,z = n[0],n[1],n[2]
m = z - y
maxi = m/x
print(int(maxi))
