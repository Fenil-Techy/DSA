class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)
        min_len = float('inf')
        window_sum = 0
        left = 0

        for right in range(n):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len

    
nums=[2,3,1,2,4,3]
target=7
s=Solution()
print(s.minSubArrayLen(target, nums))