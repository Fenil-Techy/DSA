class Solution:
    def maxSubArray(self,arr,k):
        window_sum=0
        max_sum=-float('inf')
        for i in range(len(arr)):
            
            window_sum+=arr[i]
            
            if i>=k-1:
                max_sum=max(max_sum,window_sum)
                window_sum=window_sum-(arr[i-(k-1)])
        return max_sum

arr=[2,1,5,1,3,2]
s=Solution()
print(s.maxSubArray(arr,3))