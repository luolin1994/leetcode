#--coding:utf8--
#3 无重复字符的最长子串
#给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度

s = 'abcca'
#s = 'abcabcbb' 输出为3
#注意s='' s=' '的情况
def lengthOfSubstring(s):
    if len(s) == 0:
        return 0
    res = 1
    left = 0
    right = 0
    windows = dict()    #windows中键为出现的字符，值为字符的索引位置
    while (right < len(s)):
        if s[right] in windows:   #当字符重复时，找到该字符在字典中的索引值，删除字典中left到该索引值的字符，并跳转left到该索引的下一个
            temp = windows[s[right]]
            res = max(res,right - left)
            while (left <= temp):  #使用list, 通过切片,找到字符时跳过该重复窗口
                windows.pop(s[left])
                left += 1             #可改进，是否当left到字符串尾的距离小于res时就可以停止搜索？
        else:
            res = max(res,right-left+1)

        windows[s[right]] = right
        right += 1

    return res


def le(s):
    if not s: return 0
    left = 0
    lookup = set()
    n = len(s)
    max_len = 0
    cur_len = 0
    for i in range(n):
        cur_len += 1
        print(cur_len)
        while s[i] in lookup:
            lookup.remove(s[left])
            left += 1
            cur_len -= 1
        if cur_len > max_len: max_len = cur_len
        lookup.add(s[i])
    return max_len


print(lengthOfSubstring(s))
print(le(s))
