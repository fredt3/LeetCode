class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #match fibonacci sequence
        return self.fibo(n+1)
        
    def fibo(self, x):
        if(x <= 0):
            return 0
        if(x == 1):
            return 1
        return self.fibo(x-1) + self.fibo(x-2)

print(Solution().climbStairs(5))