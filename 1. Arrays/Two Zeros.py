class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        indexes = []
        for index,num in enumerate(nums):
            indexes.append(index)
            rem_val = target - num

            i = index+1
            while i!=n:
                if rem_val == nums[i]:
                    indexes.append(i)
                    return indexes
                i = i+1
            indexes.pop()
        