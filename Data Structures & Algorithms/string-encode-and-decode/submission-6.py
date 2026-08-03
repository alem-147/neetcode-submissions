import base64

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            chunk = string + "00110"
            encoded += chunk
        return encoded
    

    def decode(self, s: str) -> List[str]:
        if s:
            return s.split("00110")[:-1]
        else:
            return []