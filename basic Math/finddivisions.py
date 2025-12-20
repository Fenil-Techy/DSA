class Solution:
    def Divisions(self, n):
        i = 1
        l = []
        while i * i <= n:
            if n % i == 0:
                l.append(i)
                if (n // i) != i:   # avoid duplicate when i*i == n
                    l.append(n // i)
            i += 1
        
        l.sort()   # sort divisors
        print(l)

d = Solution()
d.Divisions(50)


            
'''# class Solution:
#     def Divisions(self,n):
#         for i in range(1,n+1):
#             if(n%i==0):
#                 printt(i)
# d=Solution()
# d.Divisions(50)'''