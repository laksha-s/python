def printTriangle(row):
    for i in range(1, row):
        for j in range(1, i):
            print(j, end =" ")
        print()
printTriangle(10)
