class Solution(object):

    def separateDigits(self, nums):

        list1 = []
        newlist = []

        for x in range(0, len(nums)):

            k = nums[x]

            while k > 0:
                t = k % 10
                list1.append(t)
                k = k // 10

            list1.reverse()

            newlist = newlist + list1

            list1 = []

        return newlist


# Main code
nums = [13, 25, 83, 77]

solution = Solution()

answer = solution.separateDigits(nums)

print("Original list:", nums)
print("Separated digits:", answer)