class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        l, r = 0, len(s) -1
        ls, rs = "", ""
        while l <= r:
            print(l, r)
            print(s)
            while not s[l].isalnum() and l != r:
                l += 1
            while not s[r].isalnum() and r != l:
                r -= 1
            ls += s[l].lower()
            rs += s[r].lower()
            l += 1
            r -= 1
        return ls == rs
