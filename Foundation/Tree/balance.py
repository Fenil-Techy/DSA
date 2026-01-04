class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def isBalanced(self, root):
        return self.checkHeight(root) != -1

    def checkHeight(self, root):
        if not root:
            return 0 

        left_h = self.checkHeight(root.left)
        if left_h == -1: return -1  
        
        right_h = self.checkHeight(root.right)
        if right_h == -1: return -1 
        
        if abs(left_h - right_h) > 1:
            return -1
            
        return max(left_h, right_h) + 1

    
root=Node(1)
root.left=Node(2)
root.right=Node(2)
root.left.left=Node(3)
root.left.right=Node(3)
root.right.left=Node(4)
root.right.right=Node(4)

s=Solution()
print(s.isBalanced(root))