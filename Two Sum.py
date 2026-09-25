class Solution(object):

    def twoSum(self, nums, target):
        list2 = []

        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    list2.append(x)
                    list2.append(y)
                    return list2


# Create Solution object
solution = Solution()

# Input
nums = [2, 7, 11, 15]
target = 9

# Call function
result = solution.twoSum(nums, target)

# Print result
print(result)