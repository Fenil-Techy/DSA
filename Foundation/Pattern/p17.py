class Solution:
    def pyramid(self, n):
        for i in range(1, n+1):
            ch=ord('E')
            for j in range(i-1,-1,-1):
                print(chr(ch - j), end="")
            print()
s = Solution()
s.pyramid(5)
'''
E
DE
CDE
BCDE
ABCDE
'''