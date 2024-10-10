** Problem 7 LeetCode

***Method for Completing

Using a list/stack I know you are able to reverse a string or an integer due to it's 
first in last out nature.

First we need to check if x < 0 or not.
    If so make negation = -1 so we can negate the result later.
    Also we need to make x positive so we don't have to worry about
    the negative value while manipulating the integer/string.

Now, we traverse the integer as a string and append each place value
into the stack.

While s1 is true we pop all the values from the stack
turning each string back to an integer.

Now we do negation.

Check for if the integer is within bounds for an 32-bit integer

Return the result.
