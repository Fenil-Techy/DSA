'''
1             1 

1 2         2 1

1 2 3     3 2 1

1 2 3 4 4 3 2 1
'''
class Solution:
    def pattern(self, n):
        for i in range(1,n):
            for j in range(1,i+1):
                print(j,end=" ")
            for j in range(n-i-1):
                print(" ",end=" ")
            for j in range(n-i-1):
                print(" ",end=" ")
            for j in range(i,0,-1):
                print(j,end=" ")
            print("\n")
s = Solution()
s.pattern(5)