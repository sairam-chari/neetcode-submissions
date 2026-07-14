class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        dp[0].append([])
        for num in nums:
            for i in range(num,target+1):
                for comb in dp[i-num]:
                    dp[i].append(comb+[num])
        return dp[target]

