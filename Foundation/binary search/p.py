class Solution():
    def search(self,arr,target):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if(target==arr[mid]):
                return mid
            elif(target<arr[mid]):
                 high=mid-1
            else:
                low=mid+1
        return -1
    
arr = [2, 5, 7, 9, 12, 15, 18]
target=9
s=Solution()
print(s.search(arr,target))

