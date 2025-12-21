'''
A 

B B

C C C

D D D D

E E E E E

F F F F F F
'''
class Solution:
    def pattern(self, n):
        for i in range(0,n+1):
            ch=ord('A')
            for j in range(0,i+1):
                print(chr(ch+i),end=" ")
            print("\n")
s = Solution()
s.pattern(5)