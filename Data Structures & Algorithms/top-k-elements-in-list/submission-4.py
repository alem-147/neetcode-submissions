import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)
        for num in nums:
            occurances[num] += 1
        
        minheap = []
        for num, occs in occurances.items():
            heapq.heappush(minheap, (occs, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
            
        return [num for _, num in minheap]