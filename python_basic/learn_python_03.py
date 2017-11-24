# 列表学习

bicycles = ["trek", 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[2])
# print(bicycles[9])    //list index out of range
print(bicycles[-1])     # 从后位取值

bicycles[0] = "nothing"
print(bicycles)
# bicycles[4] = "test"    //IndexError: list assignment index out of range
bicycles.append("value")
bicycles.insert(7,"test")  #insert方法如果超过当前最大索引，则下标无论多大，真实下标都是当前最大下标+1
print(bicycles)

#下标删除
del bicycles[5]
print(bicycles)

#弹出
bicycles.pop(3)
print(bicycles)

# 根据值删除
bicycles.remove("nothing")
print(bicycles)

#排序
bicycles.append("aaa")
#临时排序
print(sorted(bicycles))
print(bicycles)
#逆序打印
print(bicycles.reverse())
#永久排序
bicycles.sort()
print(bicycles)
#逆序
bicycles.sort(reverse=True)
print(bicycles)
print(len(bicycles))

#循环输出
for bicycle in bicycles:
    print(bicycle)


for index in range(len(bicycles)):
    print(bicycles[index])


numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 3))
print(even_numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#列表解析
squares = [value**2 for value in range(1,11)]
print(squares)

#切片

print(numbers[:2])

#元组 ——不可变的列表

dimensions = (200, 50)
print(dimensions)
# dimensions[0] = 90   #TypeError: 'tuple' object does not support item assignment

dimensions = (20)      #元组不能更改值，但是元组变量可以重新定义值
print(dimensions)
