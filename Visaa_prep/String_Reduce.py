def str_red(s):
    if not s:
        return ""
    r = []
    c = 1
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            c+=1
        else:
            r.append(s[i-1]+str(c))
            c=1
    r.append(s[-1]+str(c))
    return ''.join(r)
s = input()
print(str_red(s))
