class Solution:
    def __init__(self):
        self.list_matrix = []
        
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if matrix == []:
            return self.list_matrix
        
        m = len(matrix)
        n = len(matrix[0])
        
        if m == 0 and n == 0:
            return self.matrix
        
        if m == 1 and n == 1:
            self.list_matrix.append(matrix[0][0])
            return self.list_matrix
        
        if m == 1:
            for i in range(n):
                self.list_matrix.append(matrix[0][i])
            return self.list_matrix
        if n == 1 :
            for i in range(m):
                self.list_matrix.append(matrix[i][0])
            return self.list_matrix
        
        for w in range(n-1):
            self.list_matrix.append(matrix[0][w])
        
        for x in range(m-1):
            self.list_matrix.append(matrix[x][n-1])
        
        for y in reversed(range(1,n)):
            self.list_matrix.append(matrix[m-1][y])
        
        for z in reversed(range(1,m)):
            self.list_matrix.append(matrix[z][0])
        
        matrix = matrix[1:m-1]
        for i in range(len(matrix)):
            matrix[i].pop(0)
            matrix[i].pop()
            
        n = matrix.count([])
        for i in range(n):
            matrix.remove([])
        print(matrix)
        self.spiralOrder(matrix)

        return self.list_matrix
        
        
            
            
        