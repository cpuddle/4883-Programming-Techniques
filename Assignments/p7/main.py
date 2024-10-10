#Collin Franklin

class Solution:
    def reverse(self, x: int) -> int:
        s1 = []
        negation = 1
        result = 0

        if x < 0:
            negation = -1
            x = -x  
            
        for i in str(x):
            s1.append(i)

        while s1:
            result = result * 10 + int(s1.pop())

        result *= negation

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result

