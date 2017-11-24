#if语句

car = "Audi"
print(car.upper())
if car.upper() != 'audi':
    print('false')
elif car.lower() == 'audi':
    print('true')


if car == 'audi':
    print('true')

else:
    print('false')



if 5 < 8 and 5 > 3:
    print('haha_true')

if 3 in range(1, 6):
    print('www_true')

if 3 not in range(1, 2):
    print('qqq_true')


test_list = []
if test_list :
    print("列表有值")
else:
    print("列表无值")


list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4]
list3 = []
list4 = [0]

# 貌似不能直接判断一个列表是否在另一个列表之中，即 子集
# if list2 in list1:
#     print("在里面")


