
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        results = [0] * len(nums)
        found_zero: bool = False

        for num in nums:
            if num == 0:
                if found_zero:
                    return [0] * len(nums)
                else:
                    found_zero = True
                    continue
            prod *= num
        
        for i, num in enumerate(nums):
            if num == 0:
                results[i] = prod
                continue
            results[i] = int(prod/num) * abs(int(found_zero) -1)

        return results
        