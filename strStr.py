#--coding:utf8--
#28 实现strStr()
# 给定一个 haystack 字符串和一个 needle 字符串，
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1
haystack = 'hello'
needle = 'll'

result = -1
for i in range(len(haystack)-len(needle)+1):
    if (haystack[i:i+len(needle)] == needle):
        result = i
        break           #刚开始忘记break

print(result)