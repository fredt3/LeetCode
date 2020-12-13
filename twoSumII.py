class Solution:
    def twoSum(self, numbers, target):
        front_ptr = 0
        back_ptr = len(numbers) - 1

        while front_ptr != back_ptr:
            sum = numbers[front_ptr] + numbers[back_ptr]
            if(sum < target):
                front_ptr += 1
            elif(sum > target):
                back_ptr -= 1
            else:
                return [front_ptr+1, back_ptr+1]

        return [front_ptr+1, back_ptr+1]


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
