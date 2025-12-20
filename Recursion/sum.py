class Solution:
    def Recursion(self,i,sum):
        if(i<1):
            print(sum)
            return;
        return self.Recursion(i-1,sum+i)
p=Solution()
p.Recursion(3,0)