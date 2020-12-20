# 704. Binary Search

class Solution:
    def search(self, nums, target):
        l_ptr = 0
        r_ptr = len(nums) - 1
        while l_ptr <= r_ptr:
            pivot = l_ptr + (r_ptr - l_ptr) // 2
            if(target < nums[pivot]):
                r_ptr = pivot - 1
            if(target > nums[pivot]):
                l_ptr = pivot + 1
            if(target == nums[pivot]):
                return pivot
        return -1


# Output: 4
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))

#Output: -1
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(Solution().search(nums, target))
