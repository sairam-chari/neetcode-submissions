class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target=len(nums)-1
        start=0
        visited=[0]*len(nums)
        q = deque()
        q.append(start)
        while q:          
            node=q.popleft()
            if node==target:
                return True
            for i in range(1,nums[node]+1):
                if node+i<len(nums) and not visited[node+i]:
                    q.append(node+i)
                    visited[node+i]=1
        return False
        