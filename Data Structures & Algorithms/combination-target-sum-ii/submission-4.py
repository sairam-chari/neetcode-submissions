class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        dp=[set() for _ in range(target+1)]
        candidates.sort()
        dp[0].add(())
        for can in candidates:
            for i in range(target,can-1,-1):
                for comb in dp[i-can]:
                    dp[i].add(comb + (can,))
        return [list(t) for t in dp[target]]


        