n = int(input())
arr1 = list(map(int,input().split(' ')))
arr2 = arr1[::-1]
for i in range(n):
    print(arr2[i],end = ' ')
