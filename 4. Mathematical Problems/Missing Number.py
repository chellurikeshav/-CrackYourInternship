class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = int((n*(n+1))/2)
        
        for i in nums:
            sum_n -= i
        
        return sum_n
        