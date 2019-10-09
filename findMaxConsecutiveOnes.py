#--coding:utf8--
#给定一个二进制数组，计算其中最大连续1的个数
#注意：输入的数组只包含0和1，其长度为正整数且不超过10000

nums = [1,1,0,1,1,1]
# 返回3
def findMaxOnes(nums):
    temp = 0
    j = 0
    for i in range(len(nums)):
        if (nums[i] == 1):
            j += 1
            if (temp<j):
                temp = j
        else:
            j = 0
    return temp

print(findMaxOnes(nums))