class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # width=len(heights-1)
        mvol = -1
        first=0
        last=len(heights)-1
        while first<last:
            vol = (last-first)*min(heights[last],heights[first])
            mvol=max(vol,mvol)
            if heights[last]>heights[first]:
                first+=1
            else:
                last-=1
        return mvol

                    

        