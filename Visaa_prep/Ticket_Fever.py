t = int(input())
for i in range(t):
    n = list(map(int,input().split(' ')))
    if n[0]>n[1]:
        m = n[0] - n[1]
        print(m)
    else:
        print("0")
