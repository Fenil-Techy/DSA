class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def __init__(self):
        self.diameter=0
    def height(self,root):
        if not root:
            return 0
        
        left=self.height(root.left)
        right=self.height(root.right)
        
        self.diameter=max(self.diameter,left+right)
        return 1+max(left,right)
    
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)

s=Solution()
print(s.height(root))
print(s.diameter)