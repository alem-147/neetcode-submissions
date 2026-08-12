class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        precompute the minimum price to that point
        and max price after that point
        the greatest difference is the best value

        how to figure out which index
        """
        n = len(prices)
        suffix_max = [0] * n 
        prefix_min = [0] * n


        prefix_min[0] = prices[0]
        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i-1], prices[i])
        
        suffix_max[-1] = prices[-1]
        for i in reversed(range(0, n-1)):
            suffix_max[i] = max(suffix_max[i+1], prices[i])

        diff = [] 
        for pre, suf in zip(prefix_min, suffix_max):
            diff.append(suf - pre)
        
        print(prefix_min)
        print(suffix_max)
        return max(0, max(diff))