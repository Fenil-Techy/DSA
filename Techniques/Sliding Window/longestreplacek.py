from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq=defaultdict(int)
        maxfreq=0
        max_len=0
        n=len(s)
        left=0
        for right in range(n):
            freq[s[right]]+=1
            maxfreq=max(maxfreq,freq[s[right]])
            while (right-left+1)-maxfreq>k:
                freq[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len

s="ABAB"
st=Solution()
print(st.characterReplacement(s,1))