#--coding:utf8--
#119 杨辉三角2
#说明：给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行

k = 3
def getrow(k):
	if k == 0:
		return [1]
	#elif k == 1:
		#return [1,1]
	else:
		lists = []
		for i in range(k+1):
			temp = []
			temp.append(1)
			for j in range(1,i):
				temp.append(lists[i-1][j-1] + lists[i-1][j])
			temp.append(1)
			lists.append(temp)
		res = lists[k]
		return res

#进阶：空间复杂度为O(K)
# j行的数据, 应该由j - 1行的数据计算出来.
# 假设j - 1行为[1,3,3,1], 那么我们前面插入一个0(j行的数据会比j-1行多一个),
# 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
def getrow2(k):
	res = [1]
	for i in range(1,k+1):
		res.insert(0,0)
		for j in range(i):
			res[j] = res[j] + res[j+1]

	return res


print(getrow2(k))

