class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxn=[]
        for first in range(len(nums)-k+1):
            maxn.append(max(nums[first:first+k]))
        return maxn


        