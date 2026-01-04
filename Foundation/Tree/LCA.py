# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root=TreeNode(3)
root.left=TreeNode(5)
root.right=TreeNode(1)
root.right.left=TreeNode(0)
root.right.right=TreeNode(6)
root.left.left=TreeNode(6)
root.left.right=TreeNode(2)
root.left.right.left=TreeNode(7)
root.left.right.right=TreeNode(4)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or p==root.val or q==root.val:
            return root
        
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        
        if left and right:
            return root
        
        return left or right

p=7
q=4
s=Solution()
result=s.lowestCommonAncestor(root,p,q)
print(result.val)
        
            
         
        