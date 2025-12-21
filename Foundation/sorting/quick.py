class Solution:
    def partition(self,arr,low,high):
        pivot=arr[high]
        i=low-1
        for j in range(low,high):
            if(arr[j]<pivot):
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[high]=arr[high],arr[i+1]
        return i+1
    
    
    def qsort(self,arr,low,high):
        if(low<high):
            pIndex=self.partition(arr,low,high)
            self.qsort(arr,low,pIndex-1)
            self.qsort(arr,pIndex+1,high)
            

arr = [4, 3, 7, 1, 5]
s=Solution()
s.qsort(arr,0,len(arr)-1)
print(arr)