n=int(input())
if n<=10000:
    d=0.80*n
    h=0.20*n
    g=d+h+n
    print("%.2f"%(g))
elif n<=20000:
    d=0.90*n
    h=0.25*n
    g=d+h+n
    print("%.2f"%(g))
elif n>20000:
    d=0.95*n
    h=0.30*n
    g=d+h+n
    print("%.2f"%(g))
    