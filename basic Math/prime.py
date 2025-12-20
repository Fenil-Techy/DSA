class Solution:
    def isPrime(self, n):
        if n <= 1:
            print("not prime no")
            return

        i = 2
        while i * i <= n:
            if n % i == 0:
                print("not prime no")
                return
            i += 1
        
        print("prime no")

s=Solution()
s.isPrime(3)
            