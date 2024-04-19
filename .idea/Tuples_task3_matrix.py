mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
diag1 = []
diag2 = []
for i in range(len(mtx)):
    diag1.append(mtx[i][i])
j = -1
for i in range(len(mtx)):
    diag2.append(mtx[i][j])
    j = j - 1
print (diag1)
print (diag2)