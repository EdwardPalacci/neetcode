class Solution:
    def removeVowels(self, s: str) -> str:
        answer = ""
        for char in s:
            if char not in "aeiou":
                answer = answer + char
        return answer
