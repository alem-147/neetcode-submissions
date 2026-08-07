class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphas = []
        for c in s:
            if not c.isalnum():
                continue
            alphas.append(c.lower())
        back_alphas = alphas[::-1]
        return back_alphas == alphas
        
