# class Solution:
#     def isPalindrome(self,str):
#         left=0
#         right=len(str)-1
#         while left<right:
#             if not str[left].isalnum(): 
#                 left+=1
#             elif not str[right].isalnum():
#                 right+=1
#             else:
#                 if(str[left]==str[right]):
#                     left+=1
#                     right-+1
#                 else:
#                     return False
#             return True
        
# str="racecaR"
# s=Solution()
# print(s.isPalindrome(str.lower()))


class Solution:
    def isPalindrome(self,s):
        left=0
        right=len(s)-1
        while left<right:
            if s[left] is not s[left].isalnum():
                left+=1 
            elif s[right] is not s[right].isalnum():
                right-=1 
            else:
                if s[left].lower()==s[right].lower():
                    left+=1
                    right-=1
                else:
                    return False
        return True
        
str="racecaR"
s=Solution()
print(s.isPalindrome(str.lower()))