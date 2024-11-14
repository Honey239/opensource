n = list(map(int,input().split(' ')))
x,y,z = n[0],n[1],n[2]
if z > x:
    if z >= x + y:
        print("2")
    else:
        print("1")
else:
    print("0")
