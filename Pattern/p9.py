class Solution:
    def pattern(self, n):
        for i in range(0,n):
            for j in range(0,i):
                print("*", end="")
            print("\n")
        for i in range(0,n):
            for j in range(0,n-i):
                print("*", end="")
            print("\n")
s = Solution()
s.pattern(5)