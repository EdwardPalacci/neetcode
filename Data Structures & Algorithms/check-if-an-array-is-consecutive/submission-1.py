class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if (nums[i] == nums[i+1] or nums[i+1] - nums[i] != 1):
                return False
        return True