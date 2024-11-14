n = list(map(int,input().split(' ')))
a,b,c,x = n[0],n[1],n[2],n[3]
if a+b>=x or b+c>=x or a+c>=x:
    print("YES")
else:
    print("NO")
