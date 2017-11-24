class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性： name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('while', 6)
print(my_dog.name)
print(my_dog.age)
print(my_dog.sit())
print(my_dog.roll_over())


class Play():
    """定义一个玩乐类"""
    def __init__(self, time=60):
        self.time = time

    def play_time(self):
        print("玩乐时间是："+str(self.time))

#继承
class MDog(Dog):

    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size
        self.play = Play()

    def printSize(self):
        """打印小狗的size"""
        print(self.size)


    def sit(self):
        """重写父类方法"""
        print("重新来sit")

m_dog = MDog('SH', 12, 24)
m_dog.printSize()
m_dog.sit()
m_dog.play.play_time()