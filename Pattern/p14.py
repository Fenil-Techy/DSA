class Solution:
    def pattern(self, n):
        for i in range(1,n+1):
            ch=ord('A')
            for j in range(n,i-1,-1):
                print(chr(ch),end=" ")
                ch+=1
            
            print("\n")
s = Solution()
s.pattern(5)