#-coding:utf8--
#567 字符串的排列
#给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
#换句话说，第一个字符串的排列之一是第二个字符串的子串。
#输入: s1 = "ab" s2 = "eidbaooo"   输出：True    解释：s2 包含 s1 的排列之一 ("ba").
s1 = "abcdxabcde"
s2 = "abcdeabcdx"
def boolInclusion(s1,s2):
    left = 0
    right =0
    windows = dict()
    needs = dict()
    for i in s1:
        needs[i] = needs.get(i,0) + 1
    while(right < len(s2)):
        c = s2[right]
        if c not in needs:
            windows.clear()
            right += 1
            left = right
        else:
            windows[c] = windows.get(c,0) + 1
            if (right - left +1 == len(s1)):
                if windows == needs:  #不比较整个dict(),而是比较符合的元素个数count== len(needs)?
                    return True
                windows[s2[left]] -= 1
                left += 1
            right += 1
    return False

print(boolInclusion(s1,s2))
