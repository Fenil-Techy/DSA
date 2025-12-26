class Solution:
    def longestSubarray(self,arr, k):
        left = 0
        window_sum = 0
        max_len = 0

        for right in range(len(arr)):
            window_sum += arr[right]

            while window_sum > k:
                window_sum -= arr[left]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
arr=[1,-1,0]
s=Solution()
print(s.longestSubarray(arr,7))
