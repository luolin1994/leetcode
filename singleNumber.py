# 136 只出现一次的数字
#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#说明： 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 解析：
# 1 交换律
# 2 任何数与0（按位）异或都为该数
# 3 相同数异或为0
# 因此 异或同一个数两次，原数不变


nums = [4,1,2,1,2]
a = 0 #定位指标

for num in nums:
    a = a ^ num

print(a)

# 利用数学的方法
#print(2*sum(set(nums))-sum(nums))



