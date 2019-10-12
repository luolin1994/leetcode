#--coding:utf8--
#给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数
#Do not return anything, modify nums in-place instead.使用空间复杂度为 O(1) 的 原地 算法

nums = [1,2,3,4,5,6,7]
k = 3
'''
#超出时间限制,暴力法
def rotate(nums,k):
    i = 1
    while(i <= k):
        temp = nums[len(nums)-1]
        for j in range(len(nums)):
            temp,nums[j] = nums[j],temp
        i += 1
'''

#反转法，先将全部值反转，再分别反转
def rotate(nums,k):
    k = k %len(nums)  #
    nums.reverse()
    rev(nums,0,k-1)
    rev(nums,k,len(nums)-1)


#反转数组的一部分
def rev(nums , start ,end):
    while start < end:
        #temp = nums[start]
        #nums[start] = nums[end]
        #nums[end] = temp
        nums[start],nums[end] = nums[end],nums[start]
        start += 1
        end -= 1



rotate(nums,k)
print(nums)


