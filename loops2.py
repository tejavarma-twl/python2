rows = int(input("Enter size : "))
a = 1
while a<=rows:
    b = rows
    c = 1
    while b>=a:
        print(" ",end=" ")
        b -= 1
    while c<=a:
        print(c,end=" ")
        print(" ",end=" ")
        c += 1
    a += 1
    print("")
