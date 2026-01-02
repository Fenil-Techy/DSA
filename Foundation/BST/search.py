class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class BST:
    def __init__(self,root=None):
        self.root=root
    
    def insert(self,root,val):
        if not root:
            return Node(val)
        
        if val<root.data:
            root.left=self.insert(root.left,val)
        else:
            root.right=self.insert(root.right,val)
        
        return root
    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
    
    def search(self,root,val):
        if not root:
            return False
        if root.data==val:
            return True
        
        if val<root.data:
            return self.search(root.left,val)
            
        else:
            return self.search(root.right,val)
       


values = [10, 5, 20, 3, 7, 15]

bst = BST()
root = None
for v in values:
    root = bst.insert(root, v)
bst.inorder(root)
print(bst.search(root,20))
