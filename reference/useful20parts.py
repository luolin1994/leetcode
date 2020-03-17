#--coding:utf8--
#20个python代码片段

#1. 字符串的翻转
#方法1
str1 = "hello world"
print(str1[::-1])
#方法2
from functools import reduce
print(reduce(lambda x,y:y+x,str1))

#2. 判断字符串是否是回文
str2 = "abccba"
def fun(string):
    if string == string[::-1]:
        print("该字符串是回文字符串")
    else:
        print("该字符串不是回文字符串")
fun(str2)

#3. 单词大小写
str3 = "i love python"
print(str3.title()) #单词首字母大写
print(str3.upper()) #所有字母大写
print(str3.capitalize()) #字符串首字母大写


#4. 字符串的拆分
str4 = "I love python"
str4_1 = "I/love/python"
str4_2 = "     I love python        "
print(str4.split())  # 默认按照空格进行拆分，返回的是列表
print(str4_1.split('/'))
print(str4_2.strip())  #默认去除字符串左右两边的空格，返回字符串
print(type(str4_2.strip()))

#5. 将列表中的字符串合并
list1 = ['I', 'love', 'python']
print(' '.join(list1))
#去除字符串中不需要的字符
import re
str5 = "I/ love. python"
print(' '.join(re.split('\W+',str5))) #\W 为非单词字符


#6. 寻找字符串中的唯一元素
str6 = "wwwweeerftttg"
print(''.join(set(str6)))
#对于列表的筛查
list2 = [2,4,5,6,7,1,2]
print(list(set(list2)))




#7. 将元素进行重复
str7 = "python"
list3 = [1,2,3]
#乘法表述
print(str7*2)
print(list3*2)

str7_1 = ""
list3_1 = []
#加法表述
for i in range(2):
    str7_1 += str7
    list3_1.extend(list3)
print(str7_1)
print(list3_1)

#8. 基于列表的扩展
list4 = [2,2,2,2]
print([2*x for x in list4])
#列表的展开
list5 = [[1,2,3],[4,5,6],[4,3],[1]]
print([i for k in list5 for i in k])


#9. 将列表展开
#方法1
from iteration_utilities import deepflatten
list6 = [[12,5,3],[2,4,[5],[6,9,7]],[5,8,[9,[10,12]]]]
print(list(deepflatten(list6)))
#方法2
def flatten1(lst):
    res = []
    for i in lst:
        if isinstance(i,list):
            res.extend(flatten1(i))
        else:
            res.append(i)
    return res
print(flatten1(list6))



#10. 二值交换
a = 1
b = 2
#方法1
a,b = b,a  #Python里的变量并不直接存储值，是引用一个内存地址。交换变量，其实是交换了引用的地址。
print(a,b)
#方法2
c = a + b
a = c - a
b = c - b
print(a,b)


#11. 统计列表中元素的频率
from collections import Counter
list7 = ['P','p','Y','y','t','t','h','o','o','o','n']
count = Counter(list7)
print(count)
print(count['P'])
print(count.most_common(1))
#手动实现
dict1 = {}
for i in list7:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(max(dict1,key=lambda x:dict1[x]))



#12. 判断字符串所含元素是否相同
str8_1 , str8_2 , str8_3 = "qwert" , "qwert" ,"ertyu"
cn1 , cn2 ,cn3 = Counter(str8_1) , Counter(str8_2) ,Counter(str8_3)
if(cn1 == cn2 and cn2 == cn3):
    print("三个字符串所包含的元素相同")


#13. 将数字字符串转化为数字列表
str9 = "2356346"
#方法1
list9_1 = list(map(int,str9))
print(list9_1)
#方法2
list9_2 = [int(i) for i in str9]
print(list9_2)


#14. 使用try-except-finally模块
a = 1
b = 4
try:
    a.append(b)
except AttributeError as e:
    print(" 'a' 不是一个列表")
else:
    print(a)
finally:
    print("程序结束")



#15. 使用enumerate()函数来获取索引-数值对
str10 = "Python"
list10 = [1,2,3,4,5]
for i , j in enumerate(str10):
    print(i,j)
for i , j in enumerate(list10):
    print(i,j)



#16.代码执行消耗时间
import time
start = time.time()
num = 0
for i in range(1000000):
    num = i
print("共消耗时间：",time.time()-start,"s")



#17. 检查对象的内存占用情况
import sys
str11 = "a"
str11_1 = "aaffg"
num1 = 32
print(sys.getsizeof(str11))
print(sys.getsizeof(str11_1))
print(sys.getsizeof(num1))



#18. 字典的合并
dict2 = {'a':1,'b':2}
dict3 = {'c':3,'d':4}
#方法1
combined_dict = {**dict2 , **dict3} #遇到重复数据，前面的值会被后面的值给取代
print(combined_dict)
#方法2
dict2.update(dict3)
print(dict2)


#19. 随机采样
import random
str12 = "wewewe"
list12= [1,2,4,5,6]
n_samples = 3
print(random.sample(list12,n_samples))
print(random.sample(str12,n_samples))


#20. 检查唯一性
str13 = [1,2,3,4,5,6]
str13_1 = [1,2,2,4,5,6]

def ifunique(seq):
    if(len(seq) == len(set(seq))):
        print("该列表中的元素是唯一性的")
    else:
        print("该列表中的元素不是唯一性的")
ifunique(str13)
ifunique(str13_1)