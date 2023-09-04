n=str(input())
k=0
c=0

for i in n:
    if i in "aeiou":
        c=c+1
        if c>k:
            k=c
    
    else:
        
        c=0
print(k)