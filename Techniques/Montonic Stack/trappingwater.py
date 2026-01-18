class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack=[]
        n=len(height)
        water=0
        for i in range(n):
            while stack and height[stack[-1]]<height[i]:
                mid=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                width=i-left-1
                h=min(height[left],height[i])-height[mid]

                water += width*h
            stack.append(i)
        return water
                