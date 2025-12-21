class Solution:
    def Recursion(self, n):
        if n <= 1:
            return 1
        return n * self.Recursion(n - 1)
p = Solution()
print(p.Recursion(3))
