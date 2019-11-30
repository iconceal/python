# tuple1=(1,2,3,4,5,6)
# print(tuple1)
# tuple=(1,)
# print(tuple1[::2])
# for index,item in enumerate(tuple1+tuple):
#    print(index,item)
# print(2 in tuple1)
# print(2 not in tuple1)
# sale=[int(i*5) for i in tuple1]
# print(sale)
# number=(i for i in range(4))
# print(number.__next__())
# print(number)
# for i in number:
#     print(i,end=' ')
# set1={1,2,3}
# set1.remove(2)
# print(set1)
# set1.update([x*3 for x in range(10)])
# print(set1)
# list=[1,2,3,4,5,67]
# set=set(list)
# print(set)
# list.pop()
# set.pop()
# print(set)
# print(set.pop())
# print(list)
# print(list.pop())
#person={
#     'name':'lyb',
#     'age':21...}
# print(person['name'])
# name = person.get('name')
# print(name)
# for key,value in person.items():
#     print(key,':',value)
# def abc(a):
#     a=a+1
#     return a
# c=2
# c=abc(c)
# print(c)
# def info(**kwargs):
#     for key in kwargs.keys():
#         value=kwargs.get(key)
#         print(key,value)
# info(name='zhangsan')
# a=10
# print(a)
# def fun():
#     global a
#     a=a+1
# fun()
# print(a)
#--------------------递归------------------
# def fib(n):
#     if n <= 0:#检查异常
#         return -1
#     if n==1 or n==2:#1递归的出口
#         return 1
#     return fib(n-1)+fib(n-2)#进入下一层的方式
# for i in range(1,21):
#     print(fib(i))
#------------------------------
# from functools import partial
# def add(a,x,b):
#     return a*x+b
# line=partial(add,2,b=3)
# a=line(9)
# print(a)
#----------生成器-------------
# a=10
# def count():
#     b=a+1
#     print(b)
#     yield 1
#     b=a*6
#     print(b)
#     yield 2
# for i in count():
#     print(i)
# count()
#-----------生成器---------------
# def fac(n):
#     a=1
#     for i in range(1,n+1):
#         a*=i
#         yield a
# fac(10)
# for x in fac(10):
#     print(x)
#   -------生成器------
# def ji():
#     #5,3,3/1
#     for cock in range(0, 20):
#         for hen in range(0, 34):
#             chicken = 100 - cock - hen
#             if cock * 5 + hen * 3 + chicken / 3 == 100:
#                 yield cock,hen,chicken
# for cock,hen,chicken in ji():
#     print('%d只公鸡%d只母鸡%d只小鸡' % (cock,hen,chicken))
#---------------------排序--------------------------------

#-------------排序------------------------
# import random
# list=[]
# for i in range(10):
#     list.append(random.randint(0, 100))
# a=list[0]
# b=list[1]
# c=list[2]
# d=list[3]
# print('原序列',a,b,c,d)
# while True:
#     if c>d:
#         c,d=d,c
#     if b>c:
#         b,c=c,b
#     if a>b:
#         a,b=b,a
#     if a<b<c<d:
#         break
#     else:
#         continue
# print('小到大',a,b,c,d)
#--------闭包----------
# def adder(x):
#     def wrapper(y):
#         return x + y
#     return wrapper#这个返回值
#
# adder5 = adder(5)
# # 输出 15
# adder5(10)#adder(5)(10)
# # 输出 11
# adder5(6)#adder(5)(6)
# print(adder5(10),adder5(6))
#------------------装饰器--------------------
# import time
# # 定义一个计时器
# def timeit(function):
#     '''
#        timeit函数负责返回一个wrapper，wrapper的参数要与原来的myfunc保持相同
#        这样一来，执行 myfunc=timeit(myfunc)  myfunc完全等价于wrapper
#        wrapper函数负责添加额外功能
#     '''
#     def wrapper():
#         start = time.clock()
#         function()
#         end = time.clock()
#         print(f'函数执行所花费的时间为：{end - start}')
#     return wrapper
# # myfunc=timeit(myfunc)  #注意，这里与前面的 “myfunc=timeit”是有所区别的哦
# # 原来的函数myfunc
# @timeit
# def myfunc():
#     print("我是函数myfunc")
# myfunc()  # 还和原来调用myfunc()一样,但是达到了添加额外功能的效果
#----------------单例模式---------------------------
# def ClassDecorator(cls):  # 第一层函数decorator
#     height = 170
#     weight = 65
#     def wrapper(name, age):  # 第二层函数wrapper，参数要和类的构造函数匹配
#         s = cls(name, age)
#         s.height = height  # 添加两个额外属性
#         s.weight = weight
#         return s  # 返回创建的对象，因为类的构造函数是要返回实例的，即有返回值
#     return wrapper
# @ClassDecorator
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# stu = Student('张三', 25)
# print(stu.name)
# print(stu.age)
# print(stu.height)  # 在 IDE中可能会有提示此处错误，学生没有height和weight属性，但是运行之后没错
# print(stu.weight)
#--------------有参数的装饰器-----------------------------
# import time
# def wrapper(param):
#     def myfunc(fun):
#         def myfunc1(*args,**kwargs):
#             print(param)
#             start = time.clock()
#             a=fun(*args,**kwargs)
#             end = time.clock()
#             print(f'函数所花费的时间为 ：{end - start}')
#             return a
#         return myfunc1
#     return myfunc
# @wrapper('lalala')
# def fun(a,b,c,d,e):
#     res=a/b*c*d/e
#     print(res)
#     return res
# fun(1,2,3,4,5)
#-----------------课堂练习------------------------
# def browse(param):#装饰器的参数
#     def browse_fun(fun):#被装饰的函数
#         def browse_in(*args,**kwargs):
#             if param.endswith('cn'):
#                 print('欢迎来到', param)
#             elif param.endswith('com'):
#                 print('welcome to', param)
#             elif param.endswith('jp'):
#                 print('未满18岁禁止访问')
#             fun(*args,**kwargs)
#         return browse_in
#     return browse_fun
# @browse('http://www.sina.com.cn')
# def fun1():
#     pass
# fun1()
# @browse('http://www.google.com')
# def fun2():
#     pass
# fun2()
# @browse('http://www.kawayi.jp')
# def fun3():
#     pass
# fun3()
#-------------------------------------
# class Cat:
#     #初始化
#     def __init__(self,name):
#         self.__name=name#姓名
#         self.__age=0#年龄
#     #过了一年
#     def yearPass(self):
#         self.__age
#     def getAge(self):
#         return self.__age
#     def __getAge(self):
#         self.__age=age
#     def __str__(self):
#         desc='%s,%d岁'%(self.__name,self.__age)
#         return desc
# cat1=Cat('哆啦A梦')
# cat1.yearPass()
# cat1._Cat__age=12312321
# print(dir(cat1))
# print(cat1)
#---------------------------------------
# class Yao(object):
#     def __init__(self,name):
#         self.name = name
#     def getName(self):
#         return self.name
# class Sheyao(Yao):
#     def __init__(self,name):
#         super().__init__(name)
# class Baishe(Sheyao):
#     def __init__(self,name):
#         super().__init__(name)
# class Qingshe(Sheyao):
#     def __init__(self,name):
#         super().__init__(name)
# class Fahai(object):
#     def __init__(self,name):
#         self.name=name
#     def catch(self,yao):
#         print(self.name+'抓'+yao.getName())
# class Man(object):
#     def __init__(self,name):
#         self.name=name
#     def love(self,obj):
#         print(self.name+'喜欢'+obj.getName())
#
# fahai=Fahai('法海')
# qingshe=Qingshe('小青')
# baishe=Baishe('小白')
# fahai.catch(qingshe)
# fahai.catch(baishe)
# xuxian=Man('许仙')
# xuxian.love(baishe)
#--------------重载运算符-------------------------
# class Point(object):
#     def __init__(self, x, y , z):
#         self.__x = x
#         self.__y = y
#         self.__z = z
#     def getPoint(self):
#         return self.__x, self.__y, self.__z
#     def __str__(self):
#         return '%d,%d,%d' % (self.__x, self.__y, self.__z)
#     # 重载加号操作符 point+point =
#     def __add__(self, other):
#         if isinstance(other, Point):#判断other是否是Point的对象
#             otherX, otherY, otherZ = other.getPoint()
#             newX = self.__x + otherX
#             newY = self.__y + otherY
#             newZ = self.__z + otherZ
#             return Point(newX, newY, newZ)
# p1 = Point(1,2,3)
# p2 = Point(7,8,9)
# p3 = p1 + p2
# print(p3)
#------------------异常处理——————————
# try:
#     input1=input('请输入被除数：')
#     value1=int(input1)
#     input2=input('请输入除数：')
#     value2=int(input2)
#     result=value1/value2
#     print(result)
# except ValueError as e:
#     print('输入值错误。',e)
# except ZeroDivisionError as e2:
#     print('除错误',e2)
# except:
#     print('其他错误')
# else:
#     print('一切正常')
# finally:
#     print('程序结束')
#---------------------------
# def div(a,b):
#     result = a / b
#     return result
# try:
#     a = 3
#     b = 0
#     result = div(a,b)
#     print(result)
# except ZeroDivisionError as e:
#     print('计算机出现被除为0的情况')
# #-----------------------------------
# class InputError(Exception):
#     def __init__(self):
#         self.length=lenth
#         self.atleast=atleast
# try:
#     inputStr=input('请输入用户名：')
#     if len(inputStr)<6:
#         raise InputError(len(inputStr),6)
# except InputError as err:
#     print('出现了异常 用户输入的长度为%d，系统要求的长度为%d'%(len(inputStr),6))
# else:
#     print('输入正常')
#-----------------------异常处理---------------------------
#import re
# import math
# ipaddr = '192.168.8.49'
# result = re.sub('\.', ' ', ipaddr)
# print(result)
#
# phone = '130-1159-2390'
# result = re.sub('-', '', phone)
# print(result)
# str = '9+6' # 待匹配的字符串
# pattern = '(.*)\+(.*)' # 表示匹配任意多个字符
# result = re.search(pattern, str)
# if result != None:
#     print('匹配成功。匹配的整个表达式是：', result.group(0))
#     print('匹配的第1部分是：', result.group(1))
#     print('匹配的第2部分是：', result.group(2))
# class Stack(object):
#     def __init__(self):
#         self.items=[]
#
#     def is_empty(self):
#         return self.items==[]
#     def size(self):
#         return len(self.items)
#     def push(self,item):
#         self.item.append(iten)
#
#     def pop(self):
#         return self.items.pop()
#     def peek(self):
#         try:
#             return self.items[len(self.items)-1]
#         except IndexError as e:
#             print(e)
# if __name__=='__main__':
#     stack=Stack()
#     print(stack.is_empty())
#     print(stack.size())
#     print('----------------')
#     stack.push('zhangsan')
#     stack.push('lisi')
#     stack.push('wangwu')
#     print(stack.peek())
