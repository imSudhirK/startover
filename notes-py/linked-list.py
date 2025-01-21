class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def insertFront(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head  = new_node

    def insertEnd(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    # detect loop using two pointers
    def detectLoop(self):
        if self.head is None or self.head.next is None:
            return False
        slowptr = fastptr = self.head
        while fastptr and fastptr.next:
            slowptr = slowptr.next
            fastptr = fastptr.next.next
            if slowptr == fastptr:
                return True
        return False
    


if __name__ == '__main__':
    llist = linkedList()
    llist.head = node(9)
    llist.insertEnd(2); llist.insertEnd(4); llist.insertFront(1)
    llist.printLL()
    print(llist.detectLoop())