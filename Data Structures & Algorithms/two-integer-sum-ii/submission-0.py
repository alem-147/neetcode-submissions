class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        added = numbers[l] + numbers[r]
        while added != target:
            if added > target:
                r -=1
            if added < target:
                l += 1
            added = numbers[l] + numbers[r]
        return [l + 1, r + 1]