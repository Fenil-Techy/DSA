import math
class Solution:
    def Count(self,n):
        orginal_n=n
        count=int(math.log(orginal_n,10)+1)
        sum=0
        while(n>0):
            last_digit=n%10
            n=n//10
            sum=sum+(last_digit**(count))
        if(orginal_n==sum):
            print(orginal_n,"is a armstrong no.")
        else:
            print(orginal_n,"is a not armstrong no.")
            
c=Solution()
c.Count(371)