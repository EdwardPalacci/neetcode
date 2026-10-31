class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_set = set()
        for num in nums:
            duplicate_set.add(num)
        if len(duplicate_set) < len(nums):
            return True
        return False