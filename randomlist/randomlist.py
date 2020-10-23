import random
from typing import List
def randomlist(n):
    num=[]
    for i in range(n):
        num.append(random.randint(1,100))
    return num

if __name__ == '__main__':
    mm=randomlist(5)
    print(mm)