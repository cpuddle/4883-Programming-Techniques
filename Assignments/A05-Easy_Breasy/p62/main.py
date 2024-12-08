class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0 for i in range(n)] for i in range(m)]
        if(m==1 and n==1):
            return 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(i==m-1 and j==n-1):
                    dp[i][j]=0 
                elif(i==m-1):
                    dp[i][j]=1
                elif(j==n-1):
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
