# 1 两数之和
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

nums = [2,7,11,15]
target = 9
#输出 [0,1]
# a=[]
# for i in range(len(nums)):
#     if (target-nums[i]) in nums:
#         if nums.index(target - nums[i]) != i:
#
#             a.append(i)
#             a.append(nums.index(target - nums[i]))
#             break
#
# print(a)


# hashmap
hashmap = {}
for index, num in enumerate(nums):
    another_num = target - num
    if another_num in hashmap:
        a= [hashmap[another_num], index]
    hashmap[num] = index
print(a)
