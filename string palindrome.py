# l = int(input())
# str = input()
# len1 = 0
# str1 = ""
# len2 = 0
# l2 = 0
# str4 = ""
# list1 = []
# list2 = []
# def palindrome(str2):
#     strrev = ""
#     for i in range(0, len(str2)):
#         strrev =  str2[i] +strrev
#     if (strrev == str2):
#         return True
#     else:
#         return False
# while len1 != l :
#     len2 = l
#     while len2 != 0:
#         str1 = ""
#         str1 = str[len1:len2]
#         if palindrome(str1):
#             if l2 <=len(str1):
#                 l2 = len(str1)
#                 list1.append(str1)
#         len2 = len2 - 1
#     len1 = len1 + 1
# for i in range(0,len(list1)):
#     if len(list1[i])== l2:
#         list2.append(list1[i])
# list2 = sorted(list2)
# str4 = list2[0]
# print(l2)
# print(str4)








triples = [ (x,y,z) for x in range(1,4) for y in range(2,5) for z in range(5,8) if x+y > z ]


print(triples)