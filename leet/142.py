# Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/description/

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def appendNode(self, data):
        newnode = node(data)
        if self.head is None: self.head = newnode; return newnode
        lastnode = self.head
        while lastnode.next: lastnode = lastnode.next
        lastnode.next = newnode; return newnode

def detectCycle(head):
    if head is None or head.next is None: return head
    slowp = fastp = head
    while fastp and fastp.next:
        slowp, fastp = slowp.next, fastp.next.next
        if slowp == fastp : break
    else: return None
    while head != slowp:
        head, slowp = head.next, slowp.next
    return head



if __name__ == '__main__':
    llist = linkedList()
    llist.appendNode(3); 
    start_cycle = llist.appendNode(2)
    llist.appendNode(0); 
    end_node = llist.appendNode(4)
    end_node.next = start_cycle
    ans =  detectCycle(llist.head)
    print("Cycle starts at: ", ans.data)




