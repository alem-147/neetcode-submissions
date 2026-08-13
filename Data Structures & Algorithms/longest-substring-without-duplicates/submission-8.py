class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        sliding window 
        - expand the window by checking delta in set length
        before and after
        - if not in set, add and continue
        - else compare to max, move left pointer
        """
        max_len = 0
        l = 0
        window_set = set()
        for r, c in enumerate(s):
            if c in window_set:
                max_len = max(max_len, len(window_set))
                while s[l] != c:
                    window_set.remove(s[l])
                    l += 1
                l += 1
            else:
                window_set.add(c)
        return max(max_len, len(window_set))
