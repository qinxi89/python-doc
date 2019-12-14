#Python 的元组与列表类似，不同之处在于元组的元素不能修改。
#元组使用小括号，列表使用方括号。
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

#!/usr/bin/python
# -*- coding:utf-8 -*-
# @Time    : 2019/12/14 9:27 下午
# @Author  : qinxi
# @Site    : www.iqinxi.com
# @File    : test1.py

tuple = (1,2,3,4,5,8,10)
print(tuple)       #输出内容：(1, 2, 3, 4, 5, 8, 10)

#取下标元组
tuple1 = tuple[:3]
print(tuple1)   #输出内容：(1, 2, 3)

#元组元素不可更改
tuple[1] = 11
print(tuple1)     #输出内容：TypeError: 'tuple' object does not support item assignment







