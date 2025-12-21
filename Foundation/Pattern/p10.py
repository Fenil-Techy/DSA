'''
Docstring for Python.Pattern.p10
1 

0 1

1 0 1

0 1 0 1
'''
class Solution:
    def pattern(self, n):
        start=1
        for i in range(0,n):
            if(i%2==0):
                start=0
            else:
                start=1
            for j in range(0,i):
                print(start,end=" ")
                start=1-start
            print("\n")
s = Solution()
s.pattern(5)