## Problem 1281 - LeetCode

### Method for Completing

Initialization:

    sum1 = 0: This variable will hold the sum of the digits.
    pro = 1: This variable will hold the product of the digits. We start with 1 because multiplying by 1 doesn't change the result (starting with 0 would make the product 0 immediately).
    num = 0: This is used to temporarily store the last digit of the number n during each iteration (not essential but helps in understanding the logic).

While Loop:

    The while loop runs as long as n > 0. In each iteration, we:
        Extract the last digit of n using n % 10. The modulo operator (%) gives the remainder of dividing n by 10, which is the last digit of n.
        Add this digit (num) to the sum1 to keep track of the sum of the digits.
        Multiply the pro (product) by this digit (num) to keep track of the product of the digits.
        Update n by removing the last digit using integer division (n // 10), which gives the quotient when n is divided by 10 (effectively removing the last digit).

Returning the Result:

    Once all digits of n have been processed (i.e., when n becomes 0), the while loop ends.
    Finally, the function returns the difference between the product (pro) and the sum (sum1) of the digits, i.e., pro - sum1.
