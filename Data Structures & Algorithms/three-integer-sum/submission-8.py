class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        trips=[]
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            first=i+1
            second=len(nums)-1
            while first<second:
                ssum=nums[i]+nums[first]+nums[second]
                if ssum==0:
                    trips.append([nums[i],nums[first],nums[second]])
                    while first<second and nums[first]==nums[first+1]:
                        first+=1
                    first+=1
                    while first<second and nums[second]==nums[second-1]:
                        second-=1
                    second-=1
                elif ssum<0:
                    first+=1
                elif ssum>0:
                    second-=1
        return trips