class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for idx, x in enumerate(nums):
            if(x == target):
                return idx
            if(x > target):
                return idx
            
        return len(nums)