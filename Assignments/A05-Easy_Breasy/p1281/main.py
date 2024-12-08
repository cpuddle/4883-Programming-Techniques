class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum1=0
        pro=1
        num=0
        while n>0:
            num=n%10
            sum1 = sum1 + num
            pro = pro * num
            n = n//10
        return pro-sum1
