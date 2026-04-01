import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        x = 0
        y = int(math.sqrt(c))
        while x <= y:
            sumSquar = x * x + y * y
            if sumSquar == c :
                return True
            elif sumSquar < c:
                x +=1
            else:
                y -=1
        return False