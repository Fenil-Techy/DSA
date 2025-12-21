import math
class Solution:
    def Count(self,n):
        orginal_n=n
        rev=0
        while(n>0):
            last_digit=n%10
            n=n//10
            rev=(rev*10)+last_digit
        if(orginal_n==rev):
            print(orginal_n,"is a palindrome")
        else:
            print(orginal_n,"is a not palindrome")
            
c=Solution()
c.Count(121)