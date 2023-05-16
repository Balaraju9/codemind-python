import math

a,b,c=map(int,input().split())

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("%.2f"%(area))
