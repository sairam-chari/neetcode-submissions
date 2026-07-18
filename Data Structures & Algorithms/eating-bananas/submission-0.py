class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        min_k=max(piles)
        # mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            time = 0 
            for pile in piles:
                time+=math.ceil(pile/mid)
            if time<=h:
                min_k=mid
                right=mid-1
            else:
                left=mid+1
            # else:

        return min_k