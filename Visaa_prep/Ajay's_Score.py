t = int(input())
for i in range(t):
    x, n = map(int,input().split())
    score_pass = (x // 10) * n
    print(score_pass)
