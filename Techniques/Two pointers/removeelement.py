class Solution:
    def remove_element(self,arr,val):
        i=0
        for j in range(len(arr)):
            if(arr[j]!=val):
                arr[i]=arr[j]
                i+=1
            
        return arr[:i]
arr=[0,1,2,2,3,0,4,2]
s=Solution()
print(s.remove_element(arr,2))