class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_row_idx = 0
        high_row_idx = len(matrix)
        

        def _binary_search(ar: list, target: int) -> bool:
            l = 0
            r = len(ar)

            while l < r:
                mid = l + (r-l) // 2
                if ar[mid] < target:
                    l = mid + 1
                elif ar[mid] > target:
                    r = mid
                else:
                    return True
            return False


        while low_row_idx < high_row_idx:
            mid_row_idx = low_row_idx + (high_row_idx - low_row_idx) // 2
            bottom_val = matrix[mid_row_idx][0]
            top_val = matrix[mid_row_idx][-1]

            if bottom_val <= target and top_val >= target:
               return _binary_search(matrix[mid_row_idx], target)

            elif bottom_val > target:
                high_row_idx = mid_row_idx
            else:
                low_row_idx = mid_row_idx + 1
        return False
