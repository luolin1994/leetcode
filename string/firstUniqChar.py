# --coding:utf8--
#387 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 注意事项：您可以假定该字符串只包含小写字母。
s = "leetcode"
# 输出0


dict = {}
for i in range(len(s)):
    if s[i] in dict:
        dict[s[i]] = len(s)+i
    else:
        dict[s[i]] = i

if len(dict) == 0:
    index = -1
else:
    index = dict.get(min(dict,key=dict.get))

    if index >= len(s):
        index = -1

print(index)

def firstUniq2(s):
    #先假设最小索引为最后的字符索引
    min_unique_char_index = len(s)

    # 已知字符串由小写字母构成，则遍历a-z
    # alpha = [chr(x) for x in range(97, 97+26)]
    for c in "abcdefghijklmnopqrstuvwxyz":
        i = s.find(c)
        # 分别从目标的字符串头和字符串尾查找对应字母的索引；如果两索引相等，则说明是单一字符
        if i != -1 and i == s.rfind(c):
        # 更新最新的最小索引
          min_unique_char_index = min(min_unique_char_index, i)
         # 如果返回值不为最后字符的索引，则返回最小索引值 # 否则，根据题意，返回-1
    return min_unique_char_index if min_unique_char_index != len(s) else -1

print(firstUniq2(s))


