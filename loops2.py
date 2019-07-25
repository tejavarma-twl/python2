# rows = int(input("Enter size : "))
prime = []
for x in range(1,50):
    for j in range(2,x):
        if x%j==0:
            break
    else:
        prime.append(x)
# print(len(prime)-1) # print(prime)
rows = len(prime)-1
a,temp,temp2 = 0,0,0
while temp2<rows:
    b = 4
    c = 0
    temp2 = temp+a
    while b>=a:             # this loop is for spacing
        print(" ",end=" ")
        b -= 1
    for i in range(temp,temp2+1):
        if i>rows:
            break
        print(prime[i],end=" ")
        print(" ",end=" ")
    print(" ")
    # print(a," ",temp," ",temp2)
    a += 1
    temp = temp+a




# rows = int(input("Enter size : "))
# a = 1
# while a<=rows:
#     b = rows
#     c = 1
#     while b>=a:
#         print(" ",end=" ")
#         b -= 1
#     while c<=a:
#         print(c,end=" ")
#         print(" ",end=" ")
#         c += 1
#     a += 1
#     print("")
