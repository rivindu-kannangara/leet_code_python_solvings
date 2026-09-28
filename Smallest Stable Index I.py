class Solution(object):
    def firstStableIndex(self, nums, k):

        for x in range(0, len(nums)):

            maximum = max(nums[:x+1])
            minimum = min(nums[x:])

            lowestdif = maximum - minimum

            if lowestdif <= k:
                return x

        return -1


# Main part
nums = [1, 3, 5, 2, 4]
k = 3

solution = Solution()

answer = solution.firstStableIndex(nums, k)

print(answer)