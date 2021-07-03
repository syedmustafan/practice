matrix = []
def spirallyTraverse(R,C):
    result = []
    for j in range(R):
        row = list(map(int, input().split()))
        matrix.append(row)
            
    print("Inputted Matrix", matrix)
    temp1 = 0 
    temp2 = 1
    temp3 = -1
    temp4 = 0
    temp5 = 0
    temp6 = 0
    for ref in range(3) : 
        for i in range(temp1, C):
            result.append(matrix[temp6][i])
        for j in range(temp2, R):
            result.append(matrix[j][C-1])
        for k in range(C-2, temp3, -1):
            result.append(matrix[R-1][k])
        for l in range(R-2, temp5, -1):
            result.append(matrix[l][temp4])
        C -= 1
        R -= 1
        temp1 += 1 
        temp2 += 1
        temp3 += 1
        temp4 += 1
        temp5 += 1
        temp6 += 1
   
    return result
R = int(input("Enter The Number of Rows: "))
C = int(input("Enter The Number of Columns: "))
print(spirallyTraverse(R,C))
