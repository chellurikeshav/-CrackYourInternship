class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        
        nums.sort()
        for i in range(1,n):
            count+=nums[i]-nums[0]
        
        return count
            
            