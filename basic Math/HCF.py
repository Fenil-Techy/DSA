'''class Solution:
    def findHCF(self,a,b):
        while a>0 and b>0:
            if(a>b):
                a=a%b
            else:
                b=b%a
        if(a==0):
            print(b)
        else:
            print(a)
s=Solution()
s.findHCF(20,40)'''

class Solution:
    def findHCF(self,n):
        even=[]
        odd=[]
        for i in range(1,(n*2)+1):
            if(i%2==0):
                even.append(i)
            else:
                odd.append(i)
        a=sum(even)
        b=sum(odd)
        print(a)
        print(b)
        
        while a>0 and b>0:
            if(a>b):
                a=a%b
            else:
                b=b%a
        if(a==0):
            print(b)
        else:
            print(a)
            
        
s=Solution()
s.findHCF(5)