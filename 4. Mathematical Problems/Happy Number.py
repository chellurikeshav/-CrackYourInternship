class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        
        repeat_n = []
        n_str = str(n)
        len_n = len(n_str)
        
        while n not in repeat_n:
            repeat_n.append(n)
            n = 0
            for i in n_str:
                n += int(i)**2
            n_str = str(n)
            len_n = len(n_str)
        
        if n!=1:
            return False
        else:
            return True
            
        
           
    
    