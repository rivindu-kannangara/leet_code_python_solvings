class Solution(object):

    def maxProduct(self, n):

        if n < 0:
            print("error")
            return 0

        list1 = []

        while n > 0:
            x = n % 10
            list1.append(x)
            n = n // 10

        list1.sort(reverse=True)

        k = list1[0] * list1[1]

        return k


# Main part
n = int(input("Enter a number: "))

solution = Solution()

answer = solution.maxProduct(n)

print("Maximum product:", answer)