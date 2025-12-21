class Solution:
    def sortt(self,arr):
        n=len(arr)
        
        for i in range(n-1):
            max_value=i
            for j in range(i+1,n):
                if(arr[j]>arr[max_value]):
                    max_value=j
            temp=arr[i]
            arr[i]=arr[max_value]
            arr[max_value]=temp
        print(arr)

arr=[7,2,5,1]
s=Solution()
s.sortt(arr)
    