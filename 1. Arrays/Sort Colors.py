class Solution:
    def sortColors(self, nums: list[int]) -> None:
        n = len(nums)
        
        for i in range(1,n):
            key = nums[i]
            j = i-1
            while key<nums[j] and j>=0:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key