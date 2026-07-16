class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrows,ncols = len(matrix),len(matrix[0])
        def check(val):
            return matrix[val//ncols][val%ncols]
        first=0
        last=nrows*ncols-1
        while (first<=last):
            mid=(first+last)//2
            if check(mid)<target:
                first=mid+1
            elif check(mid)>target:
                last=mid-1
            elif check(mid)==target:
                return True
        return False

