n = int(input())
arr = list(map(int,input().split()))
u = []
for i in arr:
    if i not in u:
        u.append(i)
print(*u)
