# class Solution:
#     def maxSubArray(self,arr,k):
#         window_sum=0
#         max_sum=-float('inf')
#         for i in range(len(arr)):
            
#             window_sum+=arr[i]
            
#             if i>=k-1:
#                 max_sum=max(max_sum,window_sum)
#                 window_sum=window_sum-(arr[i-(k-1)])
#         return max_sum

class Solution:
    def maxSubArray(self,arr,k):
        window_sum=sum(arr[:k])
        min_sum=window_sum
        n=len(arr)
        start=0
        for i in range(k,n):
            window_sum+=arr[i]
            window_sum-=arr[i-k]
            if window_sum<min_sum:
                min_sum=window_sum
                start=i-k+1

        return min_sum,arr[start:start+k]


arr=[2,1,5,1,3,2]
s=Solution()
print(s.maxSubArray(arr,3))