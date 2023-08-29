n=int(input())
n=str(n)
if '6' in n:
    n=list(n)
    p=n.index('6')
    n[p]='9'
    g="".join(n)
    print(int(g))
else:
    print(int(n))