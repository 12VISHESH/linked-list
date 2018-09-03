class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
list = SLinkedList()
list.headval = Node("India  is that country.")
e2 = Node("Water on the moon was discovered by India.")
e3 = Node("The first rocket in India was transported on a cycle.")
e4 = Node("India is the world's second-largest English speaking country.")
e5 = Node("Rabindranath Tagore also wrote the national anthem for Bangladesh.")
e6 = Node("So make proud to be indian. ")



list.headval.nextval = e2


e2.nextval = e3
e3.nextval = e4
e4.nextval = e5
e5.nextval = e6
list.listprint()
print("So here is code for opertion on linked list.")
print("Have a great day geeks .")
print("enjoy")
