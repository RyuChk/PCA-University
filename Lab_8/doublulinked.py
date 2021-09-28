class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.preverious = None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.length = None
        self.tail = None
    
    def insert(self,Node):
        temp = self.head
        if self.head == None:
            self.head = Node
        else:
            while temp.next != None:
                temp = temp.next 
            temp.next = Node
            Node.preverious = temp
    
    def insertAfter(self, PointerNode, Node):
        temp = self.head
        while temp.next != None:
            if temp.data == PointerNode.data:
                Node.next = temp.next 
                temp.next = Node
                return 0
            temp = temp.next
        temp.next = Node

    def deleteAfter(self, PointerNode):
        temp = self.head
        while temp.next != None:
            if temp.data == PointerNode.data:
                temp.next = temp.next.next
                return 0
        temp.next = Node

    def printAll(self):
        ls = []
        temp = self.head
        while temp.next != None:
            # print(f"Location : {temp} - Data {temp.data}")
            ls.append(temp.data)
            temp = temp.next
        ls.append(temp.data)
        return print(ls)
        # print(f"Location : {temp} - Data {temp.data}")
    
if __name__ == '__main__':
    print("hello")
    DL = DoublyLinkedList()
    for i in range(10):
        DL.insert(Node(i))
    DL.printAll()

class test(DoublyLinkedList):
    def __init__(self):
        super().__init__()