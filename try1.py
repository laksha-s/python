#10 rows right angled left justified numbers using python code
def printTriangle(rows):
    for i in range(1, rows):
        for j in range(1, i):
            print(j, end =" ")
        print()
printTriangle(10)