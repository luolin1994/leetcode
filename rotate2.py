# 48 旋转图像
#给定一个 n × n 的二维矩阵表示一个图像。将图像顺时针旋转 90 度。
#说明：你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
# input= [[1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# output = [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

#注意： n × n 的二维矩阵

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
        ]

n = len(matrix[0])
for i in range(n // 2 ):
    for j in range(n - n // 2):
        tmp = matrix[i][j]
        matrix[i][j] = matrix[n - 1 - j][i]
        matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
        matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
        matrix[j][n - 1 - i] = tmp
print(matrix)

#先转置后翻转
# for i in range(len(matrix)):
#     for j in range(i,len(matrix[0])):
#         matrix[i][j] , matrix[j][i] = matrix[j][i] ,matrix[i][j]
#
# for row in matrix:
#     row.reverse()
#
# print(matrix)
















