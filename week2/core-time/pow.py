class Solution:

    def myPow(self, x: float, n: int) -> float:
        result = 1
        for i in range(abs(n)):
            result *= x
        return result


solution = Solution()
print(solution.myPow(2.00000, 10))
