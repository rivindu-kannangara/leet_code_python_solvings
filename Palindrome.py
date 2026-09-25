class Solution(object):
    def isPalindrome(self, x):
        list = []
        value = 1
        
        if x < 0:
           return False

        while x > 0:
            y = x % 10
            list.append(y)
            x = x//10
        

        for k in range(0 , len(list)):
            if(list[k] != list[len(list)-k-1]):
                value = 0
                break
            else:
                continue

        if(value == 1):
            return True
        else:
            return False

k = int(input("enter number"))
i = isPalindrome(k)
print(i)