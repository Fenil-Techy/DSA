class Solution:
    def nextGreater(self,num):
        stack=[]
        res=[-1]*len(num)
    
        for i in range(len(num)):
            while stack and num[i] > num[stack[-1]]:
                index=stack.pop()
                res[index]=num[i]
            stack.append(i)
        return res

num=[4, 2, 1, 3]
s=Solution()
print(s.nextGreater(num))
        
        