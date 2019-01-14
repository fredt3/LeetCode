class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if(x>0):
            sX = str(x)
            ans = ""
            for i in range(len(sX)-1,-1,-1):
                ans += sX[i]
            if(int(ans) > 2147483647):
                return int(0)
            return int(ans)
        if(x<0):
            sX = str(abs(x))
            ans = ""
            for i in range(len(sX)-1,-1,-1):
                ans += sX[i]
            if((int(ans)*-1) < -2147483648):
                return int(0)
            return int(ans)*-1
        return x

print(Solution().reverse(-123))