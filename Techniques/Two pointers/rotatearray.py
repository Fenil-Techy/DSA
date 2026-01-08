class Solution(object):
    def rotate(self,nums,k):
        n=len(nums)
        left=0
        right=n-1
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(left,right)
        reverse(0,k-1)
        reverse(k,n-1)
        return nums

nums=[1,2,3,4,5,6,7,8]
s=Solution()
print(s.rotate(nums,2))
                
            
        