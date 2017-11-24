#!/usr/bin/python
# -*- coding: UTF-8 -*-



# 函数定义
def hello():
    print ("我是李强")


# 函数
def passFunc():
    pass

# 函数参数探究
def argFunc01(str):
    print (str)


argFunc01("李强")
argFunc01(123)


def argFunc02(str):
    print (str + 99)

# argFunc02("liqiang")
argFunc02(66)

def hello2(name, sex = "小哥哥"):
    print ("Hello \n" + "\t"+name + sex)

hello2("李强")


sumS = "2" + "2"
sumN = 2 + 2
print (sumS)
print (sumN)

# strInput= raw_input("Enter your input:")
# print int(strInput) + 5

for num in range(1,20):
    print (num)

url = "djfklj{}".format(str(1))
print (url)

ary = [5 + i for i in range(1,10)]
print (ary)

# print("hahahhah" + 5)
print("hahah" + str(3))