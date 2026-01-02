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
        
    def _min_value(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current
    
    def delete(self,root,val):
        if not root:
            return None
        
        if val<root.data:
            root.left= self.delete(root.left,val)
        elif val>root.data:
            root.right= self.delete(root.right,val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp=self._min_value(root.right)
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)
        return root

values = [10, 5, 20, 3, 7, 15]

bst = BST()
root = None
for v in values:
    root = bst.insert(root, v)

bst.inorder(root)
bst.delete(root,10)

print("\nafter node deletion")
bst.inorder(root)
