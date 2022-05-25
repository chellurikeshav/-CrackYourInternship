class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        
        rows = []
        columns = []
        
        for i in range(m):
            
            if 0 in matrix[i]:
                rows.append(i)
            
            for j in range(n):
                
                if matrix[i][j]==0:
                    
                    if j not in columns:
                        columns.append(j)
        
        for row in rows:
            matrix[row] = [0]*n
        
        for k in range(m):
            
            for column in columns:
                matrix[k][column]=0
                
        
                    
        
        
        
        
                
        
                    
        