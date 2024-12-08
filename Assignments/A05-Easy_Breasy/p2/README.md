## Problem 2 - LeetCode

### Method for Completing

1. Create a temporary `ListNode` object and set it equal to `result`.
2. Initialize variables for `carry` and `total`.

3. While either `l1`, `l2`, or `carry` are true:
   - Set `total` equal to `carry`.
   - If `l1` is not null:
     - Add `l1.val` to `total`.
     - Move `l1` to `l1.next`.
   - If `l2` is not null:
     - Add `l2.val` to `total`.
     - Move `l2` to `l2.next`.

4. Calculate the ones place:
   - The value to be added to the list is `total % 10`.
   - Update `carry` to `total // 10`.

5. Create a new `ListNode` with the calculated value and set it to the next of the temporary index.

6. Move the temporary pointer to `temporary.next`.

7. Once the while loop is done, return `result`.
