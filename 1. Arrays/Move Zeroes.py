class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        k = 0
        for i in range(n):
            
            if nums[i]!=0:
                nums[k] = nums[i]
                k+=1
        
        for j in range(k,n):
            nums[j]=0
            
            
            
                    
            
            
            
        
        
            
            
            
                    
            
            
            
        