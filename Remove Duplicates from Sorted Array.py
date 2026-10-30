
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# Main part
if __name__ == "__main__":
    nums = [1, 1, 2, 2, 3, 4, 4]

    obj = Solution()
    result = obj.removeDuplicates(nums)

    print("Number of unique elements:", result)
    print("Array after removing duplicates:", nums[:result])
