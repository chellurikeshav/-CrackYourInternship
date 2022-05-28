class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        def checkPalindrome(string):
            n = len(string)
            mid = n//2
            for k in range(mid):
                if string[k]!=string[n-1-k]:
                    return False
            return True
        
        if checkPalindrome(s):
            return True
        n = len(s)
        mid = n//2
        copy = s.copy()
        for k in range(mid):
            if s[k] != s[n-1-k]:
                copy.pop(k)
                if checkPalindrome(copy):
                    return True
                else:
                    s.pop(n-1-k)
                    if checkPalindrome(s):
                        return True
                    else:
                        return False
        
        
        
            
            
            