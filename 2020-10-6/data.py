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
print(add(1,2))