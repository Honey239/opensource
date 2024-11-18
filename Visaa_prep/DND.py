n,m = map(int,input().split())
a = list(map(int,input().split()))
num1 = []
num2 = []
for i in a:
    if i%m==0:
        num1.append(i)
    else:
        num2.append(i)
print(sum(num1)-sum(num2))
