class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n=len(nums)
        res={}
        i=0
        for j in range(n):
            while nums[j] in res:
                i=res[nums[j]]
                return abs(i-j)<=k
            res[nums[j]]=j
        return False
nums= [1,2,3,1]
s=Solution()
print(s.containsNearbyDuplicate(nums,3))