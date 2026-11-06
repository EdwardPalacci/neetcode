class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 1:
            return 0
        for i in range(0, len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1