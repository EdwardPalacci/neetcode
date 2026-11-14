class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        counter = 1
        maximum = 1
        if nums == []:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0 or nums[i+1] - nums[i] == 1:
                counter += 1
                if counter > maximum:
                    maximum = counter
            else:
                counter = 1
        return maximum