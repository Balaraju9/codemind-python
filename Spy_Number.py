n=int(input())
s=0
s1=1
while(n!=0):
    r=n%10
    s=s+r
    s1=s1*r
    n=n//10
if(s==s1):
    print("Spy Number")
else:
    print("Not Spy Number")