# 350. 两个数组的交集II
# 给定两个数组，编写一个函数来计算它们的交集。
# 说明：
#     输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
#     我们可以不考虑输出结果的顺序。

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
#输出[2,2]
a = []
for num in nums1:
    if num in nums2:
            a.append(num)
            nums2.remove(num)

print(a)