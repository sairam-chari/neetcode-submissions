class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=max(nums)
        currsum = 0
        for num in nums:
            currsum+=num
            if currsum>0:
                maxsum=max(currsum,maxsum)
            else:
                currsum=0
        return maxsum