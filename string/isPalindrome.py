# --coding:utf8--
# 125 验证回文字符串
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
s =  "A man, a plan, a canal: Panama"
#s = "0P"
#当测试用例是“0P”时，两个ascii码相差为32，正好是大小写字母之差，因此不能通过判断ascii码相差为32来满足忽略字母大小写的条件


#通过ascii码来判断字母数字
def isPa(s):
    s = s.lower()
    t =[]
    for i in s:
        if 48<=ord(i)<=57 or 65<=ord(i)<=90 or 97<=ord(i)<=122:
            t.append(i)
    start = 0
    end = len(t) -1
    flag = True
    while start != end and start < end:
        if t[start] == t[end] :
            start += 1
            end -= 1
        else:
            flag = False
            break

    return flag

print(isPa(s))
