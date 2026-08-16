class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            idx = low + (high - low) // 2

            if nums[idx] == target:
                return idx
            elif nums[idx] < target:
                low = idx + 1
            else:
                high = idx - 1
        
        return -1


