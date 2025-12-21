class Solution:
    def remove_dupli(self,arr):
        if not arr:
            return 0
        i=0
        for j in range(1,len(arr)):
            if(arr[i]!=arr[j]):
                i+=1
                arr[i]=arr[j]
        return arr[:i+1]
                
        

arr=[1,1,1,2,3,3,4]
s=Solution()
print(s.remove_dupli(arr))