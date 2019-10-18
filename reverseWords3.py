#--coding:utf8--
# 557 反转字符串中的单词3
#给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
#输入: "Let's take LeetCode contest"
#输出: "s'teL ekat edoCteeL tsetnoc"

s = "Let's take LeetCode contest"


def reverseSingleWords(s):
    s = s.split()
    for i in range(len(s)):
        temp = list(s[i])
        left = 0
        right = len(temp) -1
        while left < right:
            temp[left], temp[right] = temp[right], temp[left]
            left += 1
            right -= 1
        s[i] = ''.join(temp)
    s = ' '.join(s)
    return s

def reverseSingleWords2(s):
    s = s.split(' ')
    s = s[::-1]
    s = ' '.join(s)
    s = s[::-1]
    return s


#使用front跟back指向单词的首尾，然后反转并更新两个指针的值
#若想要原地转换，则另外写一个reverse函数，将单个单词原地转换
def reverseSingleWords3(s):
    if len(s) == 0:
        return ''
    front = 0
    back = 0
    res = ''
    for i in range(len(s)):
        if s[i] != ' ':
            back += 1
        else:
            if front == 0:
                res += s[back -1::-1]+' ' #字符串切片，注意其方向和末尾的值无法取到
            else:
                res += s[back - 1:front - 1:-1]+ ' '
            front = back + 1
            back  = front

    back += 1
    res +=s[back-1:front-1:-1]
    return res



print(reverseSingleWords3(s))

