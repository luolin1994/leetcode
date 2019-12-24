# --coding:utf8--
# 7 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#说明：假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

#输入：123   输出：321
x = -21

if(x > 0):
    flag =1
else:
    flag = -1
x1 = str(abs(x))
num = list(map(int, x1))



# start = 0
# end = len(num) -1
#
#
# while start != end and end > start:
#     num[start] , num[end] = num[end] , num[start]
#     start += 1
#     end -= 1

#以上等价于
num = num[::-1]

num = ''.join(map(str,num))
result = int(num)*flag
if result > 2**31 - 1 or result < -2**31:
    result = 0

print(result)

