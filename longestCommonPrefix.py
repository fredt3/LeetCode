class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans = ""
        x =  sorted(strs, key=len)
        if(len(strs) == 0):
            return ""
        if(len(strs) == 1):
            return strs[0]
        for idx, i in enumerate(x[0]):
            tot = 0
            for j in strs:
                if(i == j[idx]):
                    tot = tot + 1
            if(tot == len(strs)):
                ans = ans + i
            else:
                return ans    
        return ans
            
print(Solution().longestCommonPrefix(["flower","flow","flight"]))