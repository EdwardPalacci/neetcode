class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [char.lower() for char in s if char.isalnum()]
        j = len(chars) - 1
        for i in range(0, len(chars)//2):
            if chars[i] != chars[j]:
                return False
            j = j - 1
        return True