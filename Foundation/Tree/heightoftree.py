class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def maxDepth(self,root):
        if not root:
            return 0
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        
        return 1+max(left,right)
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

s=Solution()
print(s.maxDepth(root))