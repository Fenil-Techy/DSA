# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self,root=None):
        self.root=root
    def insert(self,root,value):
        if not root:
            return TreeNode(value)
        
        if value<root.val:
            root.left=self.insert(root.left,value)
        else:
            root.right=self.insert(root.right,value)
            
        return root
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
            
        if p<root.val and q<root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif p>root.val and q>root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
             return root.val
            
	

vals= [6,2,8,0,4,7,9,3,5]
p = 0
q = 4
s=Solution()
root=None
for v in vals:
    root=s.insert(root,v)
        
print(s.lowestCommonAncestor(root,p,q))