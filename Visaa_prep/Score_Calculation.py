t = int(input())
for i in range(t):
    n = list(map(int,input().split()))
    x = n[0]//10
    score = x*n[1]
    print(score)
