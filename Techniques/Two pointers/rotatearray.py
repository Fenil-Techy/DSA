class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        # extra array approach
        
        # res=[0]*n
        # for i in range(n):
        #     res[(i+k)%n]=nums[i]
        # nums[:]=res
        # return nums
        
        # O(1) space approach
        def reverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        return nums

nums=[1,2,3,4,5,6,7,8]
s=Solution()
print(s.rotate(nums,2))
        