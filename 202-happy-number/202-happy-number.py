class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n!=1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in a:
                return False
            else:
                a.add(n)
        return True
        