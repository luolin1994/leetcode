#  283 移动0
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 说明
# 1.必须在原数组上操作，不能拷贝额外的数组。 2. 尽量减少操作次数。

nums = [0,1,0,3,12]

# zero_a = zero_b= nums.count(0)
# while zero_a >0:
#     nums.remove(0)
#     nums.append(0)
#     zero_b -= 1
# print(nums)

#第一次遇到非零元素，将非零元素与数组nums[0]互换，第二次遇到非零元素，将非零元素与nums[1]互换，第三次遇到非零元素，将非零元素与nums[2]，以此类推，直到遍历完数组
i = j =0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[i] , nums[j] = nums[j], nums[i]
        j += 1
print(nums)
