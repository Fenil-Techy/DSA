import math
class Solution:
    def Count(self,n):
        rev=0
        while(n>0):
            last_digit=n%10
            n=n//10
            rev=(rev*10)+last_digit
        print(rev)
c=Solution()
c.Count(77890)