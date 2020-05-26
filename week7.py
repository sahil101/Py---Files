class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return (True)
        else:
            return (False)

    def append(self, v):  # append, recursive
        if self.isempty():
            self.value = v
        elif self.next == None:
            newnode = Node(v)
            self.next = newnode
        else:
            self.next.append(v)
        return

    def insert(self, v):
        if self.isempty():
            self.value = v
            return

        newnode = Node(v)

        # Evchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)

        return

    def delete(self, v):  # delete, recursive
        if self.isempty():
            return

        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return

    def __str__(self):
        selflist = []
        if self.value == None:
            return (str(selflist))

        temp = self
        selflist.append(temp.value)

        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return (str(selflist))



    def printnodes(self):
        l1 = []
        if self.isempty():
            return 0
        else:
            temp = self
            while temp != None:
                l1.append(temp.value)
                temp = temp.next
        return l1

    def sum(self):
        if self.value == None:
            return (0)
        elif self.next == None:
            return (self.value)
        else:
            return self.value + self.next.sum()

l1 = Node(10)
l1.append(20)
l1.append(30)


print(l1.printnodes())
print(l1.sum())