class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        res=[]
        for top in words:
            for left in words:
                if left==top:continue
                if left[0]!=top[0]:continue
                for right in words:
                    if right==top or right==left:continue
                    if right[0]!=top[3]:continue
                    for bottom in words:
                        if bottom==right or bottom==left or bottom==top:continue
                        if left[3]==bottom[0] and right[3]==bottom[3]:
                            res.append((top,left,right,bottom))
        res.sort()
        return res
words = ["able","area","echo","also"]
s=Solution()
print(s.wordSquares(words))