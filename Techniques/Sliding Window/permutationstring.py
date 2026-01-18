from collections import defaultdict
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        
        freq1={}
        freq2={}
        for ch in s1:
            if ch in freq1:
                freq1[ch]+=1
            else:
                freq1[ch]=1
        left=0
        for right in range(len(s2)):
            if s2[right] in freq2:
                freq2[s2[right]]+=1
            else:
                freq2[s2[right]]=1
            if right-left+1>len(s1):
                freq2[s2[left]]-=1
                if freq2[s2[left]]==0:
                    del freq2[s2[left]]
                left+=1
            if freq1==freq2:
                return True
                
        return False

s1="ab"
s2="eidbaooo"
s=Solution()
print(s.checkInclusion(s1,s2))