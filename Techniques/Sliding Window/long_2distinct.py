from collections import defaultdict
class Solution:
    def longest_distinct_subarray(self,s):
        freq=defaultdict(int)
        left=0
        right=0
        max_len=0
        
        for right in range(len(s)):
            freq[s[right]]+=1
            
            while len(freq)>2:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            
            max_len=max(max_len,right-left+1)
        return max_len

s="abaccc"
st=Solution()
print(st.longest_distinct_subarray(s))
            
                
                
                
                
                