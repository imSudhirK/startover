class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def insertKey(self, key):
        new_node = node(key)
        if self.root is None:
            self.root = new_node
            return
        prev_node = curr_node = self.root
        while curr_node:
            if curr_node.data == key:
                return
            elif curr_node.data < key:
                prev_node = curr_node
                curr_node = curr_node.right
            else:
                prev_node = curr_node
                curr_node = curr_node.left
        if prev_node.data < key:
            prev_node.right = new_node
        else:
            prev_node.left = new_node
    
    def utilInorderDFS(self, head):
        if head is None:
            return
        self.utilInorderDFS(head.left)
        print(head.data, end=" ")
        self.utilInorderDFS(head.right)
    def inorderDFS(self):
        self.utilInorderDFS(self.root)
        print()

if __name__ == '__main__':
    bst = BST()
    bst.insertKey(9); bst.insertKey(4); bst.insertKey(5); bst.insertKey(1)
    bst.insertKey(3); bst.insertKey(6); bst.insertKey(7); bst.insertKey(0)
    bst.inorderDFS()
