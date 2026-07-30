import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurances = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            occurances[num] += 1
        for num, count in occurances.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res