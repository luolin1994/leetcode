#--coding:utf:8--
#151 翻转字符串里的单词
#输入: "the sky is blue"
#输出: "blue is sky the"
#说明：
#无空格字符构成一个单词。
#输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
#如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
#s = 'the sky is blue'
s = '  hello  world!     '
def reverse(s):
    s = s.split()
    s = reversed(s)
    '''
    left = 0
    right = len(s) - 1
    while left < right:
        s[left],s[right] = s[right],s[left]
        left += 1
        right -= 1
    '''

    s = ' '.join(s)

    #s = ' '.join(reversed(s.split()))
    return s


#O(1)空间复杂算法
def reverse2(s):
    s = s.strip() #去除首末的空各
    res = ''
    i,j = len(s)-1, len(s)
    while i>0:                #倒序遍历字符串，当第一次遇到空格时，将该字符串加入，此后依次遍历
        if s[i] == ' ':
            res += s[i+1:j] + ' '
            while s[i] == ' ':  #略过连续的空格
                i -= 1
            j = i+ 1
        i -= 1
    return res + s[:j]

print(reverse2(s))
