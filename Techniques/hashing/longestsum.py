class Solution:
    def longestSubArray_k(self,arr,k):
        left=0
        freq={}
        max_len=0
        prefix_sum=0
        
        for i in range(len(arr)):
            prefix_sum+=arr[i]
            
            if prefix_sum==k:
                max_len=i+1
            
            if prefix_sum-k in freq:
                length=i-freq[prefix_sum-k]
                max_len=max(max_len,length)
            
            if prefix_sum not in freq:
                freq[prefix_sum]=i
            
        return max_len
    
arr=[1,-1,5,-2,3]
k=3
s=Solution()
print(s.longestSubArray_k(arr,k))
                