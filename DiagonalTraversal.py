#--coding:utf8--
# 498 数组对角线遍历


data = [[1,2,4],[8,16,32],[1,3,9],[3,4,16],[5,7,9]]

#a = [[1,2,3,4,5,6],[7,8,9,10,11,12]]
#data = [[1,2],[3,4],[5,6],[7,8],[9,10]]



row = len(data)
column = len(data[0])

x_axis = 0
y_axis = 0
flag = 0 #0表示向上，1表示向下
result = []
result.append(data[0][0])
print(result[0])
for i in range(1,row*column):
    if(flag == 0):
        if (y_axis == column -1):
            x_axis = x_axis + 1
            flag =1
        elif (x_axis == 0 ):
            y_axis = y_axis + 1
            flag = 1
        else:
            x_axis = x_axis - 1
            y_axis = y_axis + 1

        result.append(data[x_axis][y_axis])
        print(result[i])
    else:
        if (x_axis == row - 1):
            y_axis = y_axis +1
            flag = 0
        elif ( y_axis == 0):
            x_axis = x_axis + 1
            flag = 0
        else:
            x_axis = x_axis + 1
            y_axis = y_axis - 1

        result.append(data[x_axis][y_axis])
        print(result[i])

#print(result)

