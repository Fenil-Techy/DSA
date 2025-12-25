class Solution():
    def minSubArray(self,arr,k):
        window_sum=0
        min_sum=float('inf')
        
        for i in range(len(arr)):
            window_sum+=arr[i]
            
            if i>=k-1:
                min_sum=min(min_sum,window_sum)
                window_sum-=arr[i-(k-1)]
        return min_sum
    
arr=[2,1,5,1,3,2]
s=Solution()
print(s.minSubArray(arr,3))