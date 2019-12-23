# 242 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 你可以假设字符串只包含小写字母

s = "anagram"
t = "nagaram"

def isAna(s,t):
    dict = {}
    dict2 = {}
    for i in s:
        dict[i] = dict.get(i,0) + 1
    for j in t:
        dict2[j] = dict2.get(j, 0) + 1
    if dict == dict2:
        return True
    else:
        return False


def isAna2(s,t):
    dict = {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        dict[s[i]] = dict.get(s[i],0) + 1
        dict[t[i]] = dict.get(t[i], 0) - 1
    for val in dict.values():
        if val !=0:
            return False
    return True





print(isAna2(s,t))
