class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx = 0
        while idx < len(nums):
            if(nums[idx] == val):
                nums.pop(idx)
            else:
                idx += 1
            