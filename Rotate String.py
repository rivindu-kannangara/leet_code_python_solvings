class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        for x in range(len(s)):
            k = s[x:] + s[:x]

            if k == goal:
                return True

        return False

x = input("enter string")
y = rotateString(x)
print(y)