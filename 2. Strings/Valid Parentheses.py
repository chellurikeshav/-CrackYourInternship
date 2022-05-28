class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for i in s:
            
            if i == '(':
                check.append('(')
            if i == '{':
                check.append('{')
            if i == '[':
                check.append('[')
            
            if i == ')':
                try:
                    if check.pop() != '(':
                        return False
                except:
                    return False
            if i == '}':
                try:
                    if check.pop() != '{':
                        return False
                except:
                    return False
            
            if i == ']':
                try:
                    if check.pop() != '[':
                        return False
                except:
                    return False
        
        if check != []:
            return False
        
        return True
                
            
            
            
            
        