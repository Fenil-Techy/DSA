import math
class Solution:
    def Count(self,n):
        # count=0
        # while(n>0):
        #     n=n//10
        #     count=count+1
        # print(count)
        
        count=math.log(n,10)+1
        print(int(count))
c=Solution()
c.Count(77890)