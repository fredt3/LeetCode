class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        prev = ''
        for i in (s):
            if(i == 'I'):
                ans = ans + 1
            if(i == 'V'):
                if(prev == 'I'):
                    ans = ans + 3
                else:
                    ans = ans + 5
            if(i == 'X'):
                if(prev == 'I'):
                    ans = ans + 8
                else:
                    ans = ans + 10
            if(i == 'L'):
                if(prev == 'X'):
                    ans = ans + 30
                else:
                    ans = ans + 50
            if(i == 'C'):
                if(prev == 'X'):
                    ans = ans + 80
                else:
                    ans = ans + 100
            if(i == 'D'):
                if(prev == 'C'):
                    ans = ans + 300
                else:
                    ans = ans + 500
            if(i == 'M'):
                if(prev == 'C'):
                    ans = ans + 800
                else:
                    ans = ans + 1000    
            prev = i
        return ans
            

print(Solution().romanToInt("MCMXCIV"))