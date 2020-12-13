class Solution:
    def containsDuplicate(self, nums):
        hash = {}
        for num in nums:
            if(num in hash):
                return True
            hash[num] = num

        return False


input = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(Solution().containsDuplicate(input))
