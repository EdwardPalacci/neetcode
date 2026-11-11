class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for string in strs:
            answer = answer + string + '%%%%%'
        return answer
    
    def decode(self, s: str) -> List[str]:
        result = s.split('%%%%%')

        return result[0:-1]