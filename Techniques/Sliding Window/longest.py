# class Solution:
#     def longestSubarray_k(self,arr, k):
#         left = 0
#         window_sum = 0
#         max_len = 0

#         for right in range(len(arr)):
#             window_sum += arr[right]

#             while window_sum > k:
#                 window_sum -= arr[left]
#                 left += 1

#             max_len = max(max_len, right - left + 1)

#         return max_len
        
        
        
class Solution:
    def longestSubarray_k(self,arr,k):
        n=len(arr)
        window_sum=0
        max_len=0
        left=0
        for right in range(n):
            window_sum+=arr[right]
            while window_sum>k:
                window_sum-=arr[left]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
arr=[1,6,0,7]
s=Solution()
print(s.longestSubarray_k(arr,7))
