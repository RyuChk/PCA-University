import crypt

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    def get_next(self):
        return self.next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,Node):
        if self.head == None:
            self.head = Node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node
    
    def display_all(self):
        temp = self.head
         
        while temp.next != None:
            print(temp.data)
            temp = temp.next
        print(temp.data)
        print("--- END ---")

    def insert(self,key,Node):
        temp = self.head
        while temp.next != None:
            print(temp.data)
            if temp.data == key:
                Node.next = temp.next
                temp.next = Node
                return self.display_all()
            else:
                temp = temp.next


if __name__ == '__main__':
    L_list = LinkedList()
    for i in range(10):
        L_list.add(Node(i))
    L_list.display_all()
    L_list.insert(4, Node(33))