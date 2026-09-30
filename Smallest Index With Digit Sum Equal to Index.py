class Solution(object):

    def smallestIndex(self, nums):

        for x in range(0, len(nums)):

            sumx = 0
            t = nums[x]

            while t > 0:
                k = t % 10
                sumx = sumx + k
                t = t // 10

            if sumx == x:
                return x

        return -1


# Main code
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

solution = Solution()

answer = solution.smallestIndex(nums)

print("Smallest Index:", answer)