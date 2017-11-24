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

filename = 'programming.txt'

# w 模式下打开已存文件，会将原有内容清空。
# a 模式下打开文件，会对文件内容进行附加
with open(filename, 'a') as m_file:
    #w
    # m_file.write('I love miss tang.\n')
    # m_file.write("haha\n")

    #a
    m_file.write('coming\n')
    m_file.write('beautiful')
