class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        N = n
        if(N < 0): N = -N
        while(N > 0):
            if(N % 2 == 1): ans, N = ans*x, N-1
            else: x, N = x*x, N/2
        if(n <0): ans = 1 / ans
        return ans
