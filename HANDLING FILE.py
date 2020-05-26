
import operator
list1 = []
books_dict = {}
borrowers_dict = {}
checkouts_dict = {}
final_dict = []
sorted_dict = []

def books(a,b):
    list2 = []
    for i in range(a+1,b):
        list2  = list1[i].split("~")
        books_dict[list2[0]] = list2[1]
def borrowers(b,c):
    list2 = []
    for i in range(b + 1, c):
        list2 = list1[i].split("~")
        borrowers_dict[list2[0]] = list2[1]
def checkouts(c,d):
    list2 = []
    for i in range(c + 1, d):
        list2 = list1[i].split("~")
        checkouts_dict[(list2[0],list2[1])] = list2[2]
def sorted2(a,list4,books_dict,borrowers_dict,checkouts_dict):
    d1 = {}
    list5 = []
    d = ''
    b = ''
    c = ''
    for i in range(0, len(list4)):
        if a == list4[i][1]:
            d1[list4[i][0][1]] = (list4[i][0][0], list4[i][0][2], a)
    list5 = sorted(list((d1.keys())))
    for i in range(0,len(list5)):
        (d,b,c) = d1[list5[i]]
        print("{0}~{1}~{2}~{3}".format(b,a,list5[i],books_dict[list5[i]]))
def  sorted1(c,final_dict,books_dict,borrowers_dict,checkouts_dict):
    list4 = []
    d1  = {}
    i = 0
    a  =''
    for i in range(0,len(final_dict)):
        if c == final_dict[i][1]:
            d1[(final_dict[i][0][0],final_dict[i][0][1],c)] =  borrowers_dict[final_dict[i][0][0]]

    list4= sorted(d1.items(), key=operator.itemgetter(1))
    for i in range(0,len(list4)):
        if a != list4[i][1]:
            a = list4[i][1]
            sorted2(a,list4,books_dict,borrowers_dict,checkouts_dict)
        else:
            continue
def evaluation():
    a = ''
    final_dict= sorted(checkouts_dict.items(), key=operator.itemgetter(1))
    for i in range(0,len(final_dict)):
        if a != final_dict[i][1]:
            a = final_dict[i][1]
            sorted1(final_dict[i][1],final_dict,books_dict,borrowers_dict,checkouts_dict)
        else:
            continue







def library():
    s = ""
    while (s != "EndOfInput"):
        s = input()
        list1.append(s)
    a = list1.index("Books")
    b = list1.index("Borrowers")
    c = list1.index("Checkouts")
    d = list1.index("EndOfInput")
    books(a,b)
    checkouts(c,d)
    borrowers(b,c)
    evaluation()


library()












