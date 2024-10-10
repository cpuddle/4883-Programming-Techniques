## Problem 7 - LeetCode

### Method for Completing

Using a list/stack, we can reverse a string or an integer due to its first-in-last-out nature.

1. First, we need to check if \( x < 0 \). If so, set `negation = -1` so we can negate the result later. We also need to make \( x \) positive to avoid worrying about the negative value while manipulating the integer/string.

2. Next, we traverse the integer as a string and append each place value into the stack.

3. While the stack is not empty, we pop all the values from the stack, converting each string back to an integer.

4. Now, we apply the `negation` if necessary.

5. Check if the integer is within the bounds for a 32-bit integer.

6. Return the result.
