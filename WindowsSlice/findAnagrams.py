#--coding:utf8--
#438. 找到字符串中所有字母异位词
#给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#说明：字母异位词指字母相同，但排列不同的字符串。

s = 'cbaebabacd'
p = 'abc'
#输出：[0,6]

#s = 'abab'
#p = 'ab'

#将字典作为i计数器集合
def findAnag(s,p):
    result = []
    left = 0
    right = 0
    needs = dict()    #目标字符串中各个字符的数量
    windows = dict()  #窗口中各个字符的数量
    for i in p:
        needs[i] = needs.get(i,0) + 1  #字典的get方法，接受一个键和一个默认值作为参数。 如果字典中存在该键，则返回对应值；否则返回传入的默认值
    while right < len(s):
        temp = s[right]
        if temp not in needs:
            windows.clear()
            right += 1
            left = right
        else:
            windows[temp] = windows.get(temp,0) + 1
            if right-left + 1 == len(p):
                if windows == needs:
                    result.append(left)
                windows[s[left]] = windows[s[left]] - 1
                left += 1
            right +=1
    return result


#超出时间限制
#如何判断字串符合条件？
'''
def findAnag(s,p):
    p = sorted(p)
    result = []
    start = 0
    end = len(p)-1
    while(end < len(s)):
        temp = s[start:end+1]
        temp = sorted(temp)
        if temp == p:
            result.append(start)
        start += 1
        end += 1
    return result
'''

print(findAnag(s,p))