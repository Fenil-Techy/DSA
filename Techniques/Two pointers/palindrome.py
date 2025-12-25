class Solution:
    def isPalindrome(self,str):
        left=0
        right=len(str)-1
        while left<right:
            if not str[left].isalnum(): 
                left+=1
            elif not str[right].isalnum():
                right+=1
            else:
                if(str[left]==str[right]):
                    left+=1
                    right-+1
                else:
                    return False
            return True
        
str="racecaR"
s=Solution()
print(s.isPalindrome(str.lower()))