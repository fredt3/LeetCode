class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for indexi, numi in enumerate(nums):
            for indexj, numj in enumerate(nums[indexi+1:len(nums)], start=indexi+1):
                if numi+numj == target:
                    return [indexi, indexj]

nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))
