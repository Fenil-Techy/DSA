class Solution:
    def sortt(self,arr):
        ht={}
        for x in sorted(arr):
            ht[x]=x
    
        print(ht.values())
arr=[1,5,2,8,4,20,6,98,35,80,68]
s=Solution()
s.sortt(arr)