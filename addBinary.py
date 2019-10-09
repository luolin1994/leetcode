#--coding:utf8--
#二进制相加，但是此方法容易出现溢出现象
a = '1110'
b = '1011'
'''
c = int(a,2)
d = int(b,2)

e = c+d

f = bin(e)
f = list(f)[2:]
result = ''.join(f)
print(result)
print(type(result))
'''

ans, extra = '',0
i,j=len(a)-1,len(b)-1
while i>=0 or j>=0:
    if i >= 0:
        extra += ord(a[i]) - ord('0')  #返回对应字符的ASCII数值
    if j >= 0:
        extra += ord(b[j]) - ord('0')
    ans += str(extra % 2)
    extra //= 2      #取整除 - 向下取接近除数的整数
    i,j = i-1,j-1
if extra == 1:
    ans += '1'

ans.isalpha()
print(ans[::-1])