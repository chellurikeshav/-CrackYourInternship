class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        new_t = []
        
        for i in range(len(s)):
            if s[i] == '#':
                try:
                    new_s.pop()
                except:
                    new_s = []
            else:
                new_s.append(s[i])
        
        for j in range(len(t)):
            if t[j] == '#':
                try:
                    new_t.pop()
                except:
                    new_t = []
            else:
                new_t.append(t[j])
        
        return new_s == new_t
        
        
        