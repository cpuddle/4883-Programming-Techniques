## Problem 50 - LeetCode

### Method for Completing

The algorithm uses binary exponentiation for efficient calculation in O(log⁡n)O(logn) time.

Initialize: ans = 1 and N = |n| (absolute value of n).
Binary Exponentiation:

    While N > 0:
        If N is odd: multiply ans by x, then decrement N.
        If N is even: square x and halve N.

Handle Negative Exponent: If the original n was negative, set ans = 1 / ans.
Return: Return ans, which is xnxn.
