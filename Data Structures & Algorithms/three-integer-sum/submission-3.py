class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        triples = []
        for i, a in enumerate(nums):
            if a > 0:
                break

            l, r = i + 1, len(nums) - 1

            if i > 0 and a == nums[i - 1]:
                continue
                
            while l < r:
                summed = nums[l] + nums[r] + nums[i]
                if summed == 0:
                    triples.append([nums[i], nums[l], nums[r]])
                    l += 1 
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif summed > 0:
                    r -= 1
                else:
                    l += 1
        return triples 