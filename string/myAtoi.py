# --coding:utf8--
# 8 字符串转换整数
# 功能：实现一个atoi函数，使其能将字符串转换成整数
#说明：首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
#     当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，
#     作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
#     该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
#     注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
#     在任何情况下，若函数不能进行有效的转换时，请返回 0。
#     假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
str =  "+"

def Atoi(str):
    res = ""
    flag =1
    str = str.lstrip() #去掉左边空格
    if len(str) == 0 :
        return 0
    if str[0] == "-":
        flag = -1
    elif str[0] == "+" :
        flag = 1
    elif '0'<= str[0] <= '9':
        res += str[0]
    else:
        return 0
    for i in range(1,len(str)):
        if '0'<= str[i] <= '9':
            res += str[i]
        else:
            break

   # 如果测试用例为 “+” 或  “-”
    if len(res) >0 :
        res = int(res)
    else :
        return 0

    res = res * flag

    if res > 2**31-1:
        res = 2**31-1
    elif res < -2**31:
        res = -2**31

    return res

# 使用正则表达式
def Atoi2(s):
    import re
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
#findall函数返回所有找到的结果，用一个list表示，*是解包，因为我们的答案只有一个也就是说list中只会有一个元素，所以直接解包就可以了

print(Atoi(str))
