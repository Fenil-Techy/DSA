'''
A 

A B

A B C

A B C D

A B C D E
'''
class Solution:
    def pattern(self, n):
        for i in range(1,n+1):
            ch=ord('A')
            for j in range(i):
                print(chr(ch),end=" ")
                ch+=1
            
            print("\n")
s = Solution()
s.pattern(5)