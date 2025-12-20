class Solution:
    def sortt(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if(arr[j]>arr[j+1]):
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
                print(arr)
            print("\n")
        print(arr)
        print(arr)
arr=[8,3,5,2]
s=Solution()
s.sortt(arr)

                    
                
                
