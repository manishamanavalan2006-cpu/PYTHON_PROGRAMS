r=int(input("ENter the row value:"))
for i in range(1,r):
    for j in range(i,r+1):
        print(" ", end=" ")
    for k in range(1,i):
        print("*",end=" ")
    for j in range(1,i+1):
         print("*",end=" ")//python program to print the diamond pattern
    print()

for i in range(1,r+1):
    for j in range(1,i+1):
        print(" ", end=" ")
    for k in range(i,r):
        print("*",end=" ")
    for j in range(i,r+1):
        print("*",end=" ")
    print()


