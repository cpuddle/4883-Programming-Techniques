## Problem 62 - LeetCode

## Method for Completing

Dynamic Programming Table (dp):

    We create a 2D list dp of size m x n initialized to zero. This table will store the number of unique paths to reach each cell in the grid.

Base Case:

    If the grid is of size 1x1 (i.e., m == 1 and n == 1), there is only one path — staying at the start position. Therefore, the function immediately returns 1 for this case.

Filling the DP Table:

    The function works by filling the dp table from the bottom-right corner of the grid to the top-left corner. This is done by iterating in reverse order (starting from the bottom-right and moving towards the top-left).

    Bottom-right Corner (m-1, n-1):
        The value at dp[m-1][n-1] represents the destination (bottom-right corner), where no further movement is possible, so it is initialized to 0 (indicating no further paths from here).

    Last Row (i == m-1):
        In the last row, the only way to move is to go right. Therefore, for all j values in the last row, dp[m-1][j] is set to 1 (indicating one path to the right).

    Last Column (j == n-1):
        In the last column, the only way to move is down. Therefore, for all i values in the last column, dp[i][n-1] is set to 1 (indicating one path downwards).

    Other Cells (i != m-1 and j != n-1):
        For all other cells, the number of unique paths to reach that cell is the sum of the paths from the cell to the right (dp[i][j+1]) and the cell below (dp[i+1][j]). This is because, at each point, you can either move right or move down to get to the destination.

Final Result:

    The final number of unique paths from the top-left corner (0,0) to the bottom-right corner (m-1, n-1) will be stored in dp[0][0], which is returned at the end of the function.
