#User function Template for python3
import math
class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        min_diff = math.inf
        
        for i in range(N-M+1):
            k = A[M-1+i]-A[i]
            if k<min_diff:
                min_diff = A[M-1+i]-A[i]
        
        return min_diff
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends