n = int(input())
d = str(abs(n))
d = int(d[::-1])
if n < 0:
    d = -d
if -2**31 <= d <= 2**31 -1:
    print(d)
else:
    print(0)
