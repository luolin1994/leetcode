#--coding:utf8--
#给定长度为 2n 的数组, 你的任务是将这些数分成 n 对,
#例如 (a1, b1), (a2, b2), ..., (an, bn) ，使得从1 到 n 的 min(ai, bi) 总和最大

nums = [1,4,3,2]
result = 0
n = int(len(nums) / 2)
nums.sort()
for i in range(n):
    result = result + nums[2*i]
print(result)
