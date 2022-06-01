class Solution:
    def convertToTitle(self, c: int) -> str:
        strs = ""
        
        while c>0:
            rem = c%26
            
            if rem == 0:
                strs += "Z"
                c = c//26-1
                continue
                
            c = c//26
            strs += chr(rem+64)
    
        return strs[::-1]