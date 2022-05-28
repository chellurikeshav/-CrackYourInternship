class Solution:
    def __init__(self):
        self.output = []
    def generateParenthesis(self, n):
        i = 1
        j = 0
        s = '('
        self.ParenthesisRecursion(s,i,j,n)
        return self.output
        
    def ParenthesisRecursion(self,s,i,j,n):
        if i == n and j <=n :
            k = s + ')'*(n-j)
            self.output.append(k)
            return 0
        
        elif i == j:
            self.ParenthesisRecursion(s+'(',i+1,j,n)
        else:
            self.ParenthesisRecursion(s+'(',i+1,j,n)
            self.ParenthesisRecursion(s+')',i,j+1,n)