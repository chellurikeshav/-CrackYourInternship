class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        n = len(strs)
        min_len = 500
        for x in strs:
            if min_len>len(x):
                min_len = len(x)
                
        if min_len == 0:
            return ""
        
        common = ''
        for i in range(int(min_len)):
            key = strs[0][i]
            
            for j in range(n):
                if strs[j][i] != key:
                    return common
            
            common += key
            
        return common
            