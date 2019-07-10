print("Hello")
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))
print(a)
print(b)
print(c)

if a==b and a==c:
    print("All are equal")
elif b==c and b>a:
    print("B and c are great!")
elif b==a and b>c:
    print("B and A are great!")
elif c==a and c>b:
    print("C and A are great!")
elif a>b and a>c:
    print("A is great!")
elif b>c and b>a:
    print("B is great!")
else:
    print("C is great!")
