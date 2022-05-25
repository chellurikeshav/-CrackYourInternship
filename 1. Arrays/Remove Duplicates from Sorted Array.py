import math
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n = len(nums)
        
        k = 1
        i = 1
        key = nums[0]
        
        while i<n:
            
            if nums[i]==key:
                nums[i]=math.inf
            else:
                key = nums[i]
                k+=1

            i+=1
        
        nums.sort()
        return k
        
        
            
            
        