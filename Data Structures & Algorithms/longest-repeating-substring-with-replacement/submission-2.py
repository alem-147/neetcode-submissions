from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = defaultdict(int)
        max_freq = 0
        max_window = 0
        
        for r in range(0, len(s)):
            freqs[s[r]] += 1
            max_freq = max(max_freq, freqs[s[r]])
            while (r - l + 1) - max_freq > k:
                freqs[s[l]] -= 1
                l+=1
            max_window = max(max_window, r - l + 1)
        return max_window
            
            