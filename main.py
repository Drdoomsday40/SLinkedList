

from classSLinkedList import SLinkedList

def main():



    mySLList = SLinkedList()
    mySLList.atBeginning("Mon")
    mySLList.atBeginning("Tue")
    mySLList.atBeginning("Wed")
    mySLList.atBeginning("Thu")
    mySLList.SLListPrint()
    mySLList.RemoveNode("Tue")
    mySLList.SLListPrint()
    print("The end")

main()