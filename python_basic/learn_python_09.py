# 文件和异常

#获取文件内容，需要先open文件
#传入的参数是文件名，查找当前py文件所在目录下是否有'pi_digits.txt'文件，有则打开，
#没有的话，就会报错'No such file or directory: 'pi_digit.txt'
#with 在不再需要访问文件后将其关闭，所以没有在程序中调用close()。

# filename = 'pi_digits.txt'
# with open(filename) as file_object:
    #读取文件 并输出
    # contents = file_object.read()
    # print(contents.rstrip())
    #逐行输出
    # for line in file_object:
    #     print(line.rstrip())

    #创建包含文件的列表
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# #读取文件 并判断自己的生日是否在pi前一百万位之中
# filename = 'pi_million_digits.txt'
# with open(filename) as pi_file:
#     lines = pi_file.readlines()
#
# pi_string = ''
# for line in lines:
#     #rstrip 去除空格换行
#     pi_string += line.rstrip()
#
# birthday = input('Enter your birthday, in the form mmddyy: ')
# if birthday in pi_string:
#     print('Your birthday appears in the first million digits of pi!')
# else:
#     print('Your birthday does not appears in the first million digits of pi!')


# 写文件
# filename = 'programming.txt'
#
# # w 模式下打开已存文件，会将原有内容清空。
# # a 模式下打开文件，会对文件内容进行附加
# with open(filename, 'a') as m_file:
#     #w
#     # m_file.write('I love miss tang.\n')
#     # m_file.write("haha\n")
#
#     #a
#     m_file.write('coming\n')
#     m_file.write('beautiful')

# ###异常处理
# print('Give me two numbers, and I`ll divide them.')
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input('\nFirst number: ')
#     if first_number == 'q':
#         break
#     second_number = input('\nSecond number: ')
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         # print("You can`t divide by 0!")
#         pass
#     else:
#         print(answer)
#
#
#
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('You can not divide by zero!')


#存储数据
import json

numbers = [3,42,1,24,5,6,7,86,44,67]
filename = 'numbers.json'
#存储数据
with open(filename, 'w') as number_jsonfile:
    json.dump(numbers, number_jsonfile)

#读取数据
with open(filename, 'r') as number_readjson:
    num_json = json.load(number_readjson)

print(num_json)