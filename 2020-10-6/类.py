class student():
    def __init__(self,name,age,hight):
        self.name=name
        self.age=age
        self.hight=hight
    def study(self):
        print("{}在睡觉".format(self.name))
    def sleep(self):
        print("{}在睡觉".format(self.name))
s=student("张三",18,180)
print(s.name,s.age,s.hight)
s.sleep()
s.study()