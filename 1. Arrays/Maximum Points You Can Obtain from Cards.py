class Solution:
    
    def maxScore(self, cp: List[int], k: int) -> int:
        
        n = len(cp)
        
        if k == n:
            return sum(cp)
        
        n = n-1
        max_val = sum(cp[:k])
        check = max_val
        
        while k>0:
            
            check += (-cp[k-1]+cp[n])
            max_val = max(max_val,check)

            n -= 1
            k -= 1
            
        return max_val
            
        