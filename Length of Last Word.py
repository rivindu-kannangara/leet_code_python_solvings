class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])


# Main part
s = input("Enter a string: ")

obj = Solution()
result = obj.lengthOfLastWord(s)

print("Length of last word:", result)