#--coding:utf8--
#54 螺旋矩阵
#输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#首次提交未考虑到break
data = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

result = []

row = len(data)
column = len(data[0])
iter = int((min(row,column) + 1) / 2)
x = 0
y = 0

for i in range(0,iter):
    x = i
    for y in range(i, column - i):
       result.append(data[x][y])
    if x+1 < row - i:
            while x + 1 < row - i:
                    x = x + 1
                    result.append(data[x][y])
            if y > i:
                    while y > i:
                            y = y - 1
                            result.append(data[x][y])
                    if x-1 > i:
                            while x - 1 > i:
                                    x = x - 1
                                    result.append(data[x][y])
                    else:
                            break

            else:
                    break
    else:
            break




print(result)


'''
r, i, j, di, dj = [], 0, 0, 0, 1
if matrix != []:
    for _ in range(len(matrix) * len(matrix[0])):
        r.append(matrix[i][j])
        matrix[i][j] = 0
        if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
            di, dj = dj, -di
        i += di
        j += dj
'''
