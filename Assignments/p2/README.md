** Problem 2 LeetCode

***Method for Completing

Create a temporary ListNode object and set that temporary ListNode equal to result. 
As well as creating variables for carry and total.

While list one, list 2, or carry are true
set total equal to carry

if l1 is true
add l1.val to total

do the the same for l2

then, to get the ones place we do a modulus on total
the number value that is returned to the list is equal to the total % 10
now to get the tens place we do integer division to cut off the ones value and set that equal to carry
carry = total // 10

make ListNode(num) equal to the next temporary index
then move temporary to temporary.next

once the while loop is done, return the result
