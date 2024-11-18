n = int(input())
a = list(map(int,input().split()))
left = 0
right = 0
for i in range(n):
    if i!=0 or i!=n:
        left += sum(a[0:i])
        right += sum(a[i+1:n+1])
        r = abs(left - right)
        print(r,end = " ")
        left,right = 0,0
    elif i==0:
        left = 0
        right += a[i+1:n+1]
        r = abs(left - right)
        print(r,end = " ")
    else:
        right = 0
        left += a[0:n]
        r = abs(left - right)
        print(r,end = " ")
print()
