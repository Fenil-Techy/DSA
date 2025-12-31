class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def inorder(self,root):
        if not root:
            return 
        
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
        
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

s=Solution()
print(s.inorder(root))