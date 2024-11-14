n = int(input())
a = n - (n * (10/100))
b = n - 100
if a < b:
    print(int(a))
else:
    print(b)
