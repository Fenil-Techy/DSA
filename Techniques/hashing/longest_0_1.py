class Solution:
    def longestSubArray_k(self,nums):
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            
        freq={}
        max_len=0
        prefix_sum=0
        k=0
        
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            
            if prefix_sum==k:
                max_len=i+1
            
            if prefix_sum-k in freq:
                length=i-freq[prefix_sum-k]
                max_len=max(max_len,length)
            
            if prefix_sum not in freq:
                freq[prefix_sum]=i
            
        return max_len
    
        # balance=0
        # max_len=0
        # freq={0:-1}
        
        # for i in range(len(nums)):
        #     if nums[i]==1:
        #         balance+=1
        #     else:
        #         balance-=1
            
        #     if balance in freq:
        #         length=i-freq[balance]
        #         max_len=max(max_len,length)
        #     else:
        #         freq[i]=balance
        return max_len
nums = [0,1,1,1,1,1,0,0,0]
s=Solution()
print(s.longestSubArray_k(nums))
                