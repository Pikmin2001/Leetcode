class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        
        while l <= r:
            mid = (l+r) // 2
    
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        #this should be the target row   

        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l+r) // 2
            if target == matrix[mid][m]:
                return True
            elif target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
        return False  