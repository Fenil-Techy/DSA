class Solution:
    def longestSubArray_k(self,arr):
        # for i in range(len(arr)):
        #     if arr[i]==0:
        #         arr[i]=-1
        # print(arr)
            
        # freq={}
        # max_len=0
        # prefix_sum=0
        # k=0
        
        # for i in range(len(arr)):
        #     prefix_sum+=arr[i]
            
        #     if prefix_sum==k:
        #         max_len=i+1
            
        #     if prefix_sum-k in freq:
        #         length=i-freq[prefix_sum-k]
        #         max_len=max(max_len,length)
            
        #     if prefix_sum not in freq:
        #         freq[prefix_sum]=i
            
        # return max_len
    
        balance=0
        max_len=0
        freq={0:-1}
        
        for i in range(len(arr)):
            if arr[i]==1:
                balance+=1
            else:
                balance-=1
            
            if balance in freq:
                length=i-freq[balance]
                max_len=max(max_len,length)
            else:
                freq[i]=balance
        return max_len
arr = [0, 1, 0, 1, 1, 1, 0]
s=Solution()
print(s.longestSubArray_k(arr))
                