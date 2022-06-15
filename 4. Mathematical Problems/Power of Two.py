class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True

        x = 1
        while x<n:
            x = x<<1
        
        return x == n
        