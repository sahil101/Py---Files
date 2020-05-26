# import itertools
# print(list(itertools.permutations([1,2,3])))




# remove duplicates from sets




a = [10,20,30,20,10,50,60,40,80,50,40]

print(sorted(set(a)))
# dup_items = set()
# uniq_items = []
# for x in a:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)
# print(uniq_items)