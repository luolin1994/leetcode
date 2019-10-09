#--coding:utf8--

matrix = [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]

r, i, j, di, dj = [], 0, 0, 0, 1
if matrix != []:
    for _ in range(len(matrix) * len(matrix[0])):
        r.append(matrix[i][j])
        matrix[i][j] = 0
        if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
            di, dj = dj, -di
        i += di
        j += dj

print(r)