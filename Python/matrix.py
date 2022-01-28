# CSCI 1030U Practice Final Exam - Programming Question #2

def multiplyMatrices(a, b):
    numOperations = 0
    n = len(a)

    # make an zero matrix
    result = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append(0)
        result.append(row)

    # multiply the matrices
    for r in range(n):
        for c in range(n):
            value = 0.0
            for i in range(n):
               # multiply the rth row, ith column in the first matrix with the ith row, cth column in the second
               value += a[r][i] * b[i][c]   # count only this line

               # count this as one multiplication
               numOperations += 1
            result[r][c] = value;

    print('numOperations:', numOperations)
    return result

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,0,0],[0,1,0],[0,0,1]]
result = multiplyMatrices(a, b)
print(result)