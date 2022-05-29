class Solution(object):
    def addBinary(self, a, b):
        a = eval('0b'+a)
        b = eval('0b'+b)
        
        return bin(a+b)[2:]
        