class Solution(object):
    def maxFrequencyElements(self, nums):
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        max_key=None
        max_value=0
        
        for key in freq:
            if(freq[key]>max_value):
                max_value=freq[key]
                max_key=key
        print(max_key,max_value)
                
        
nums=[1,2,3,1,1]
s=Solution()
s.maxFrequencyElements(nums)
        