class Solution:
    def longestEven(self,str):
    
        last_index=-1
        for i in range(len(str)):
            if str[i]=="2":
                last_index=i
        if last_index==-1:
            return "" 
                
        return str[:last_index+1]
    
str="111"
s=Solution()
print(s.longestEven(str))
                
            