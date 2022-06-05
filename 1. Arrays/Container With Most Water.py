class Solution:
    def __init__(self):
        self.max_val = 0
        
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        n = len(height)
        
        left = 0
        right = n-1
        
        while left<right:
            
            new_val = min(height[left],height[right])*(right-left)
            if max_val < new_val:
                max_val = new_val
            
            if height[left] <= height[right]:
                left+=1
            else:
                right-=1
                
        return max_val