class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def fibo(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n not in memo:
                memo[n] = fibo(n-1) + fibo(n-2)
            return memo[n]
        
        return fibo(n)