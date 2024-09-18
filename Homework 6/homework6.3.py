num: int = int(input("enter number:"))
for x in range(1, num+1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()
for x in range(num +1,1,-1):
    for y in range(1, x -1):
        print(y, end=" ")
    print()


