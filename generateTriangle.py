#--coding:utf8--
#118 杨辉三角
numRows = 5
result = []
for i in range(numRows):
    if (i == 0):
        result.append([1])
    #elif (i==1):
        #result.append([1,1])
    else:
        temp = []
        temp.append(1)
        for j in range(1,i):
            temp.append(result[i-1][j-1] + result[i-1][j])
        temp.append(1)
        result.append(temp)

print(result)
