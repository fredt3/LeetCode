import sys

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #return x**n

        if(n < 0):
            return 1/self.myPow(x, -n)
        if(n == 0):
            return 1
        if(n % 2 == 0):
            return self.myPow(x, n // 2)*self.myPow(x, n // 2)
        else:
            return self.myPow(x, n // 2)*self.myPow(x, n // 2)*x

print(Solution().myPow(float(sys.argv[1]), int(sys.argv[2])))
