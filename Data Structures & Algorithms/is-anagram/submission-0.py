class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_list = []
        s_list = []
        for letter in s:
            s_list.append(letter)
        for letter in t:
            t_list.append(letter)
        t_list.sort()
        s_list.sort()
        if s_list == t_list:
            return True
        return False

