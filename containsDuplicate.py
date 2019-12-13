# 217 存在重复元素
#给定一个整数数组，判断是否存在重复元素。
#如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

nums = [1,2,3,4]
sets = set(nums)
flag  = False
if len(sets) != len(nums):
    flag = True

# for i in range(len(nums)):
#     sets.add(nums[i])
#     if len(sets) != (i+1):
#         flag = True
#         break

print(flag)

