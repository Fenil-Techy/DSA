class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def countNodes(self,root):
        if not root:
            return 0
        
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)
        
        return 1+left+right
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

s=Solution()
print(s.countNodes(root))