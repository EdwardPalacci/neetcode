class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = {}
        for string in strs:
            altered = "".join(sorted(string))
            if altered not in answer:
                answer[altered] = [string]
            else:
                answer[altered].append(string)
        return list(answer.values())
