class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magList = list(magazine)
        for c in ransomNote:
            if c in magList:
                magList.remove(c)
            else:
                return False

        return True


ransomNote = "aa"
magazine = "aab"
print(Solution().canConstruct(ransomNote, magazine))
