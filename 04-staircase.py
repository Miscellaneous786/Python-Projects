def staircase():
    n = int(input("Enter the number of steps: "))
    for i in range(1, n):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
staircase()
