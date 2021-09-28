from doublulinked import Node,DoublyLinkedList

class squishy(DoublyLinkedList):
    def __init__(self, list):
        super().__init__()
        for i in list:
            self.insert(Node(i))
    def squish(self):
        temp = self.head
        while temp.next != None:
            if temp.data == temp.next.data:
                tn = temp.next
                temp.next = tn.next 
                del tn
            else:
                temp = temp.next
        self.printAll()
    
    def dble(self):
        temp = self.head
        while temp.next is not None:
            t = temp
            temp = temp.next
            self.insertAfter(t, Node(t.data))
        self.insertAfter(temp, Node(temp.data))
        self.printAll()

if __name__ == '__main__':
    DL = squishy([3,3,7,7,4,4,2,2,2,2])
    DL.printAll()
    DL.squish()
    DL.dble()