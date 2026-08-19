class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        l = 1
        r = max_k

        hrs_dict = defaultdict(list)

        def _hours_to_eat(k: int) -> int:
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/k)
            return hrs

        k = max_k
        while l < r:
            k = l + (r - l) // 2
            hrs = _hours_to_eat(k)
            
            if hrs > h:
                l = k + 1
            else:
                r = k
        return l

