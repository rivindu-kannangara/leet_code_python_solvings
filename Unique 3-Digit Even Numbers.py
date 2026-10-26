
class Solution(object):
    def totalNumbers(self, digits):
        numbers = set()

        for i in range(len(digits)):
            for y in range(len(digits)):
                for k in range(len(digits)):

                    if i != y and i != k and y != k:
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            x1 = str(digits[i]) + str(digits[y]) + str(digits[k])
                            numbers.add(x1)

        return len(numbers)


# Calling part
digits = [2, 1, 3, 0]

obj = Solution()
result = obj.totalNumbers(digits)

print("Total unique 3-digit even numbers:", result)
