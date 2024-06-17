def printTriangle(rows):
    for i in range(1, rows):
        for j in range(1, i):
            print(j, end =" ")
        print()
printTriangle(10)
printTriangle(20)