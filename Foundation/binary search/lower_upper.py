class Solution:
    def lower(self,arr,target):
        low,high=0,len(arr)
        while low<high:
            mid=(low+high)//2
            if(arr[mid]<target):
                low=mid+1
            else:
                high=mid
        return low
    def upper(self,arr,target):
        low=0
        high=len(arr)
        
        while low<high:
            mid=(low+high)//2
            if(arr[mid]<=target):
                low=mid+1
            else:
                high=mid
        return low
        
arr=[1,3,3,3,5,7]
s=Solution()
print(s.lower(arr,3),s.upper(arr,3))
