#--coding:utf8--
#167 两数之和2 -输入有序数组
#给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数
#函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2
#说明：返回的下标值（index1 和 index2）不是从零开始的；你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素

#错误：超出时间限制
numbers = [2,7,11,15]
target = 9

def sum_target(numbers,target):
    num = len(numbers)
    if (num < 2 or  numbers[num-1] + numbers[num-2] < target):
        return []
    result = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                result.append(i+1)
                result.append(j+1)
                return result
    return result


print(sum_target(numbers, target))
