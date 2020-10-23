import  time
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
s=time.time()

def fib2(n):
    if n==0 or n==1 or n==2:
        return n
    else:
        return fib(n-1)+fib(n-2)


def fib3(n):
    if n<=2:
        return n
    else:
        return n*fib(n-1)

# 青蛙跳台阶每次跳1阶,每次跳2阶,
# n阶台阶从n-1台阶,或者n-2台阶
# 跳上去,n-1 n-2的再依次调用
def fib4(n):
    if n<=2:
        return n
    return fib4(n-1)+fib4(n-2)
# s=time.time()
# print(fib(40))
# e=time.time()
# print(s-e)
print(fib4(5))