class Solution:
    def twosum(self,nums,target):
        n=len(nums)
        res={}
        for i in range(n):
            value=target-nums[i]
            if value in res:
                return res[value],i
            res[nums[i]]=i
nums=[3,2,4]
target = 6
s=Solution()
print(s.twosum(nums,target))