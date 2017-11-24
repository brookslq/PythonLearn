#def 函数

#形参等号两边不要有空格
def greet_user(username, nothing=''):
    """显示简单的问候语句"""
    print('hello '+ username +" " + nothing)
    return 'cool'

greet_user('brooks', 'enheng')
greet_user(username='lili', nothing='123')
greet_user(nothing='123', username='lili')

print(greet_user('bb', '22'))
print(greet_user('cc'))

#传递任意数目的实参
# 加个*，让python创建了一个空元组，并将受收到的所有值都封在了这个元组中。

def make_pizza(*toppings):
    '''打印顾客点的所有配料'''
    # print(toppings)
    for topping in toppings:
        print(topping)

make_pizza('aaaa')
make_pizza('qqqq','wwwww')

#注意 这里有两个 *
#形参名前加俩个*表示，参数在函数内部将被存放在以形式名为标识符的dictionary中，这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式。
def build_userInfo(first_name, last_name, **otherInfo):
    userInfo = {}
    userInfo["first_name"] = first_name
    userInfo["last_name"]  = last_name

    for key, value in otherInfo.items():
        userInfo[key] = value

    return userInfo


user_info = build_userInfo('brooks', 'le', location = 'beijing', field = 'physics')
print(user_info)