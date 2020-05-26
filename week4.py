# # a = { "sahil": "1DS17CS743",
# #       "GAURANG": "1DS17CS717",
# #         "ISHAN": "1DS17CS719"}
# #
# # print(a.keys())
# # print(a.values())
# # print(sorted(a.keys()))
# #
#
# def average(l,m,len1):
#     ar = 0.0
#     c  = 0
#     sum = 0
#     for j in range(0,len1):
#         if l[j][0] == m:
#             sum = sum + l[j][1]
#             c = c+1
#     ar = sum/c
#     return ar
# def rainaverage(l):
#     len1  = len(l)
#     m = 0
#     i = 0
#     list2 = {}
#     list3 = []
#     for i in range(0,len1):
#         m = l[i][0]
#         list2[m] =   average(l,m,len1)
#     for j in sorted(list2.keys()):
#         list3.append((j,list2[j]))
#     return list3
#

list2 = []
def flatten(l):
    len1 = len(l)
    for i in range(0,len1):
        if type(l[i]) == type([]):
            flatten(l[i])
        else:
            list2.append(l[i])
    return list2


# def flatten(l):
#     len1  = len(l)
#     n = 0
#     list1 = []
#     for i in range(0,len1):
#         if type(l[i]) == type([]):
#             n = len(l[i])
#             for j in range(0,n):
#                 list1.append(l[i][j])
#         else:
#             list1.append(l[i])
#     return list1

print(flatten([1,2,[3],[4,[5,6]]]))


















