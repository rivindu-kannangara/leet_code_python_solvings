
class Solution(object):
    def sumAndMultiply(self, n):
        y = str(n)
        total = 0
        k = ""

        for x in y:
            if x != '0':
                total += int(x)
                k += x

        if k == "":
            return 0

        return int(k) * total


# Main part
if __name__ == "__main__":
    n = int(input("Enter a number: "))

    obj = Solution()
    result = obj.sumAndMultiply(n)

    print("Result:", result)
