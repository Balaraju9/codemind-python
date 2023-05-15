a, b, c = map(int, input().split())
if a==b==c:
    print("Equilateral triangle")
elif a==b or a==c or b==c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
