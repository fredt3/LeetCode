class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        try:
            return len(s.split()[-1])
        except:
            return 0
        