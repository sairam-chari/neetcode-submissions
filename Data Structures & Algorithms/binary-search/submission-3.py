class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        if nums[0]==target:
            return 0
        if nums[len(nums)-1]==target:
            return len(nums)-1
        while (first<last-1):
            mid=int((first+last)/2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                first=mid
            elif nums[mid]>target:
                last=mid
        return -1
            
        