# MusicPlayer.py : this file containes the "main.py" function
# Program execution begins and ends there.
#
# The MusicPlayer is a class that is designed to create a singly linked-list
# and can start the playlist, next, prev, nextRandom, allRandom, and Clear
# functions you can call:
# InsertAtHead() = Play()
# Next() is going to next song or playing first song in list
# Prev(), repeat song
# DoubleClickPrev() is play prev
# NextRandom() will skip to the next song as random not previously chosen 
# ShufflePlaylist() all songs in playlist will be shuffled
# Clear() clears the songs that have been played so far
# ResetPlaylist() resets the playlist order to original
#
# Provided by: Lucien Maurice
# Email Address: luciencmaurice@gmail.com
# FILE: MusicPlayer.py
# CLASS PROVIDED: MusicPlayer

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class MusicPlayer:
    #
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertAtHead(self, data):
        # NewNode is created,
        # NewNode.prev is new head
        # the NewNode is now at the head
        NewNode = Node(data)
        if self.head == None:
            self.head = NewNode
        else:
            NewNode.next = self.head
            self.head = NewNode
        return ("Now playing " , data)
        # NewNode.next = self.head
        # self.head = NewNode

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total+=1
            current = current.next
        return total

    def RemoveNode(self, RemoveNode):
        # function to remove node
        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == RemoveNode):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == RemoveNode:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None

    def eraseElem(self, index):
        # function to remove an element at a certain index
        if index >= self.length():
            print("Error, Index out of Range.")
            return
        currentIndex = 0
        currentNode = self.head
        while True:
            lastNode = currentNode
            currentNode = currentNode.next
            if currentIndex == index:
                lastNode.next = currentNode.next
                return
            currentIndex+=1

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def displayArray(self):
        myArray = []
        current = self.head
        if current == None:
            print("Error, the list is empty")
            return
        while current != None:
            myArray.append(current.data)
            current = current.next
        print(myArray)

    def SLListPrint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next