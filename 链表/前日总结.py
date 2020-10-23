"""
Autbor:BAI先生
github:主页NONE
"""
print('hello,word')
def add(x,y):
    '''
    :param x:d待加的第一个元素
    :type x:int类型
    :param y:待加的第一个元素
    :type y:int类型
    :return:返回x，y的和
    :rtype:int类型
    '''
    return x+y

def add(x:int,y:int)->int:#返回值注解
    '''
    :param x:d待加的第一个元素

    :param y:待加的第一个元素

    :return:返回x，y的和

    '''
    return x+y
print(add(1,2))

def add(x:int,y:int)->int:
    '''

    :param x:
    :type x:
    :param y:
    :type y:
    :return:
    :rtype:
    '''

    try:
        return x + y
    finally:
        return  x-y
"""
Author:BAI先生
github:主页NONE
"""