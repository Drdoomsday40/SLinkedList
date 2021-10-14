# Provided by:   Lucien Maurice
# Email Address: luciencmaurice@gmail.com
# FILE: classLinkedList.py
# CLASS PROVIDED: SLinkedList

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    #
    def __init__(self):
        self.head = None

    def atBeginning(self, arg):
        NewNode = Node(arg)
        NewNode.next = self.head
        self.head = NewNode

    def RemoveNode(self, RemoveKey):
        # function to remove node
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == RemoveKey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == RemoveKey:
                break
            prev = HeadVal.next
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None

    def SLListPrint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next