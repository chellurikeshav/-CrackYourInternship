class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        neg = False
        if x < 0:
            neg = True
        
        x = str(abs(x))
        n = len(x)
        
        while n>0:
            if x[n-1] == '0':
                x = x[:n-1]
                n = n-1
            else:
                break
        val = int(x[::-1])
        
        if not (-2**(31) <= val <= 2**(31)-1):
            return 0
        
        if neg:
            return -val
        
        return int(x[::-1])
        
        
        