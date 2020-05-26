# color1 = ["Red", "Green", "Orange", "White"]
# color2 = ["Black", "Green", "White", "Pink"]
# list1 = []
# for i in color1:
#     for j in color2:
#         if i == j:
#             list1.append(i)
#
# print(list1)

# alternative solution

# similar = [0,1,2,3,4,3,2,5,6,7]
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# print(set(color1))
# print(set(similar))
# print(set(color1) & set(color2))
# list1 = [1,2,3,4]
# list2  =[1,2]
# print(list1.difference(list2))
#
# #alternate solution
# list1 = [1, 2, 3, 4]
# list2 = [1, 2]
# print(list(set(list1) - set(list2)))




#maximum number in a list




# def max_num_in_list( list ):
#     max = list[ 0 ]
#     for a in list:
#         if a > max:
#             max = a
#     return max
# print(max_num_in_list([1, 2, -8, 0]))


# frequency of a number in a list


l1 = [10,20,30,20,10,40,50,60,80,7,1,2,1,4,7]
dict = {}
count = 0

l2 = set(l1)
for i in l2:
    count = 0
    for j in l1:
        if i == j:
            count  = count +1
    dict[i] = count
print(dict)


