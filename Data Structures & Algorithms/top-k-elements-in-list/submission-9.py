class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        # We now need to extract and remove the most common value k times
        answer = []
        while len(answer) < k:
            key = max(my_dict, key=my_dict.get)
            answer.append(key)
            del my_dict[key]
        return answer



