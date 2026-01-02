class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for n in nums:
            if n in freq:
                freq[n]+=1
            else:
                freq[n]=1
            
        for i in freq:
            if freq[i]>=2:
                return i
    
nums=[1,2,3,4,5,3]
s=Solution()
print(s.repeatedNTimes(nums))