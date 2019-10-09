#--coding:utf8--
#编写一个函数来查找字符串数组中的最长公共前缀,
#如果不存在则返回空字符串

strings = ['flower','flow','flight']

def longest(strs):
    if (len(strs) == 0):
        return ''
    result = ''
    num = min(len(strs[i]) for i in range(len(strs)))
    for i in range(num):
        for j in range(len(strs)):
            if (strs[j][i] != strs[0][i]):
                return result
        result = result + strs[0][i]

    return result

print(longest(strings))





