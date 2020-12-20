# 278. First Bad Version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l_ptr = 1
        r_ptr = n

        while l_ptr <= r_ptr:
            pivot = l_ptr + (r_ptr - l_ptr) // 2
            if isBadVersion(pivot):
                r_ptr = pivot - 1
            else:
                l_ptr = pivot + 1

        return l_ptr
