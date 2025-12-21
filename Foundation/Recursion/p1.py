'''class Solution:
    def Recursion(self,n):
        if(n==0):
            return;
        print("fenil")
        return self.Recursion(n-1)
p=Solution()
p.Recursion(5)'''

class Solution:
    def Recursion(self,n):
        if(n==0):
            return;
        print(n)
        return self.Recursion(n-1)
p=Solution()
p.Recursion(5)