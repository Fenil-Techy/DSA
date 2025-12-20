class Solution:
    def nextGreater(self, nums):
        stack = []
        res = [-1] * len(nums)

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                index = stack.pop()
                res[index] = nums[i]
            stack.append(i)

        return res


nums=[4,5,10,2,8]
s=Solution()
print(s.nextGreater(nums))
        