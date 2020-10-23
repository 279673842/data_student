import time
# 辗转相除 =欧几里得
# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     while a%b!=0:
#         c=a%b
#         a=b
#         b=c
#     if b !=1:
#         return b

# # 更相减损术 =九章算术
# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     while a-b!=b:
#         c=a-b
#         if b>c:
#             a=b
#             b=c
#         else:
#             a=c
#     if b !=1:
#         return b


# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     if a-b==0:
#         return a
#
#     return commondivisor(a-b,b)
# 枚举法
# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     for i in range(b,1,-1):
#         if (a%i)==0 and(b%i)==0:
#             return i
#
# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     if a%b==0:
#         return b
#     for i in range(b//2,1,-1):
#         if (a%i)==0 and(b%i)==0:
#             return i
# # 遍历
# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     elif a==b:
#         return a
#     am=[]
#     bm=[]
#     res=[]
#     for i in range(2,a):
#         if a%i==0:
#             am.append(i)
#     for j in range(2,b+1):
#         if b % j == 0:
#             bm.append(j)
#     for m in am:
#         if m in bm:
#             res.append(m)
#     return res

# 合并
# def commondivisor(a,b):
#     if a<b:
#         a,b=b,a
#     if a/b>2:
#         while a%b!=0:
#             c=a%b
#             a=b
#             b=c
#     else:
#         while a-b!=b:
#             c=a-b
#             if b>c:
#                 a=b
#                 b=c
#             else:
#                 a=c
#     if b != 1:
#         return b
def commondivisor(a,b):
    if a<b:
        a,b=b,a
    count=0
    while a%2==0 and b %2==0:
        a=a/2
        b=b/2
        count+=1
    while a-b!=b:
        c=a-b
        if b>c:
            a=b
            b=c
        else:
            a=c
    return b*(2**count)
a=time.time()
print(commondivisor(24,16))
b=time.time()
print(a-b)