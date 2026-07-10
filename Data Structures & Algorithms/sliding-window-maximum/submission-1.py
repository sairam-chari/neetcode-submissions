class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxn=[0]*(len(nums)-k+1)

        for first in range(len(nums)-k+1):
            maxn[first]=(max(nums[first:first+k]))
        return maxn


        