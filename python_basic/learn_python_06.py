#input and while

# message = input("Tell me something, and I will repeat it back to you:")
# print(message)
#
# age = input('Tell me your age:')
# print(age)
#
# if int(age) >= 18:
#     print('大人啦~')
#
#
# print(4 % 3)
# print(5 % 3)


#### while

from python_basic import learn_python_07
from python_basic.learn_python_07 import make_pizza as makeP

learn_python_07.make_pizza('haha', 'hahahahha')

makeP('22','44444444')

current_numbers = 3
while current_numbers <= 5:
    print(current_numbers)
    current_numbers += 1
    # break

m_number = 0
while m_number < 10:
    m_number += 1
    if m_number % 2 == 0:
        continue
    print(m_number)