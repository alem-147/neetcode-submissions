class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        water = 0
        max_l = 0
        max_r = 0
        while l < r:
            if height[l] < height[r]:
                max_l = max(height[l], max_l)
                water += max_l - height[l]
                l += 1
                continue
            else:
                max_r = max(height[r], max_r)
                water += max_r - height[r]
                r -= 1
                continue

        return water