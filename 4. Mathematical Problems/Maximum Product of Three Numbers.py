class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        n = len(nums)
        
        if n==3:
            return reduce((lambda x,y:x*y),nums)
        
        nums.sort()
        
        
        if nums[0]*nums[1]*nums[n-1]>nums[n-3]*nums[n-2]*nums[n-1]:
            return nums[0]*nums[1]*nums[n-1]
        else:
            return nums[n-3]*nums[n-2]*nums[n-1]