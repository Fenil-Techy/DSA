class Solution:
    def pyramid(self, n):
        for i in range(1, n+1):
            ch=ord('A')
            # print left spaces
            for s in range(n-i):
                print(" ", end="")

            # print increasing letters
            for j in range(i):
                print(chr(ch + j), end="")

            # print decreasing letters (skip last to avoid duplicate middle)
            for j in range(i-2, -1, -1):
                print(chr(ch + j), end="")

            # move to next line
            print()

s = Solution()
s.pyramid(5)
'''
    A
   ABA
  ABCBA
'''