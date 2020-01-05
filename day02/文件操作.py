
对文件操作流程
1、打开文件，得到文件句柄并赋值给一个变量
2、通过句柄对文件进行操作
3、关闭文件 

f = open('./1.txt')        #打开文件
first_line = f.readline()
print('first_line:',first_line)      #读一行
print('我是分割线'.center(50,'-'))
data = f.read()      #读取剩下文件的所有内容，文件大时，不要用
print(data)        #打印文件

f.close()          #关闭文件

打开文件的模式有：

r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
"+" 表示可以同时读写某个文件

r+，可读写文件。【可读；可写；可追加】
w+，写读
a+，同a

"U"表示在读取时，可以将 \r \n \r\n自动转换成 \n （与 r 或 r+ 模式同使用）

rU
r+U

"b"表示处理二进制文件（如：FTP发送上传ISO镜像文件，linux可忽略，windows处理二进制文件时需标注）

rb
wb
ab


############################################# with语句 ##########################################

为了避免打开文件后忘记关闭，可以通过管理上下文，即：
with open('log','r') as f:
     
    ...
如此方式，当with代码块执行完毕时，内部会自动关闭并释放文件资源。

在Python 2.7 后，with又支持同时对多个文件的上下文进行管理，即：
with open('log1') as obj1, open('log2') as obj2:
    pass

#############################################  input 函数  ######################################

input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
例子：
while True:
  str = input("请输入：")
  print("你输入的内容是：",str)

############################################ 打开和关闭文件 #######################################
open函数，用Python内置的open()函数打开一个文件，创建一个file对象，相关的方法才可以调用它进行读写。
file object = open(file_name [, access_mode][, buffering])

File对象的属性
一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息
file.closed 	返回true如果文件已被关闭，否则返回false。
file.mode	    返回被打开文件的访问模式。
file.name	    返回文件的名称。
file.softspace	如果用print输出后，必须跟一个空格符，则返回false。否则返回true。


fo = open("foo.txt", "w")
print("文件名：", fo.name)            #output:foo.txt
print("是否已经关闭", fo.closed)       #output: False
print("访问模式：", fo.mode)           #output: w
print("末尾是否强制加空格：", fo.softspace)   #python 3中不再支持

########################################### close 函数 ########################################


























