# 36 有效的数独
#  判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
#     数字 1-9 在每一行只能出现一次。
#     数字 1-9 在每一列只能出现一次。
#     数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

#说明:
#   一个有效的数独（部分已被填充）不一定是可解的。
#   只需要根据以上规则，验证已经填入的数字是否有效即可。
#    给定数独序列只包含数字 1-9 和字符 '.' 。
#   给定数独永远是 9x9 形式的。

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]



# # 判断数字1-9是否重复
# def isDuplicate(nums):
#     hashmap = {}
#     for index , num in enumerate(nums):
#         if num != '.':
#             if num in hashmap:
#                 return False
#             else:
#                 hashmap[num] = index   #改进 将hashmap保存起来
#     return True
#
# isvalid = True
# while(True):
#     for j in range(9):
#         isvalid = isDuplicate(board[j])
#         if isvalid == False:
#             break
#     if isvalid == False:
#         break
#
#     for j in range(9):
#         isvalid = isDuplicate(board[0:9][j])
#         if isvalid == False:
#             break
#     if isvalid == False:
#         break
#
#     for j in range(3):
#         for z in range(3):
#             temp = board[3*z][3*j:3*j+3]+board[3*z+1][3*j:3*j+3]+board[3*z+2][3*j:3*j+3]
#             isvalid = isDuplicate(temp)
#             if isvalid == False:
#                 break
#         if isvalid == False:
#             break
#     break
#
#
# print(isvalid)


#遍历每一个数，判断该该数在行，列，子区域是否有重复，子区域的表示方法
def isValid(board):
    line_map = [{} for i in range(9)]
    column_map = [{} for j in range(9)]
    area_map = [{} for z in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            area_num = i//3*3 + j//3   #判断该值所属于的区域
            if num != '.':
                line_map[i][num] = line_map[i].get(num,0)+1
                column_map[j][num] = column_map[j].get(num,0)+1
                area_map[area_num][num] = area_map[area_num].get(num,0)+1

                if line_map[i][num] >1 or column_map[j][num] >1 or area_map[area_num][num] > 1:
                    return False
    return True

print(isValid(board))

