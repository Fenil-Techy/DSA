class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def preorder(self,root):
        if not root:
            return 
        
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
        
    def inorder(self,root):
        if not root:
            return 
        
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
        
    
root=Node(10)
root.left=Node(5)
root.right=Node(20)
root.right.left=Node(15)


s=Solution()
print("Pre-order Traversal:", end=" ")
s.preorder(root)

print("\nIn-order Traversal: ", end=" ")
s.inorder(root)