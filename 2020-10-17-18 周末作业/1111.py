a=[1,2,3,2,1]
b=[1,2,3,2,1]
a=a[1:4]
print(a)
b=b[3:0:-1]
print(b)
print(a==b)















# def longestPalindrome(s: str) -> str:
#     end = len(s) - 1
#     start = 0
#     for i in range(end, start - 1, -1):
#         for j in range(start, end + 1):
#             if s[i] == s[j]:
#                 if s[i:j] == s[j:i, -1]:
#                     return s[i:j + 1]


# print(longestPalindrome("babad"))