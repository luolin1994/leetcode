#--coding:utf8--
#leetcode题号：209 长度最小的字数组
#给定一个含有 n 个正整数的数组和一个正整数 s ,
#找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
#如果不存在符合条件的连续子数组，返回 0.

s = 5
nums = [2,3,1,2,4,3]
#输出为2
#问题1：超出时间限制，要求时间复杂度为O
#解决方法：窗口滑动问题

def minSubArray(s,nums):
    '''
    temp = len(nums)+1
    for i in range(len(nums)):
        sum = 0
        j= 0
        while (sum < s and j < temp):
            if (i+j > len(nums)-1):
                j = len(nums)+1
                break
            sum = sum + nums[i + j]
            j = j+1
        temp = min(temp,j)
    if (temp == len(nums)+1):
        temp = 0
    return temp
    :param s:
    :param nums:
    :return:
    '''
    temp = len(nums)+1
    count = 0
    begin = 0
    end = 0
    while(end < len(nums)):
        count += nums[end]
        end += 1
        while(count >= s):
            temp = min(temp,end - begin)
            count -= nums[begin]
            begin += 1
    if (temp == len(nums) + 1):
        temp = 0
    return temp


print(minSubArray(s,nums))