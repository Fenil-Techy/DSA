class Solution:
    def pattern(self, n):
        size = 2*n - 1
        for i in range(size):
            for j in range(size):
                top = i
                left = j
                bottom = size - 1 - i
                right = size - 1 - j
                min_dist = min(top, left, bottom, right)
                print(n - min_dist, end=" ")
            print()

s = Solution()
s.pattern(4)