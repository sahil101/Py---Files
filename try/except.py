

def largest():

    print("Maximum is {0}".format(max(list1)))
    print("Minimum is {0}".format(min(list1)))
    print(list1)

x = 0
x1 = 0
list1 = []
while  True:
    x = input("enter a number")
    if x == "done":
        largest()
        break
    try:
        x1 = int(x)
        list1.append(x1)
    except:
        print("invalid input")


