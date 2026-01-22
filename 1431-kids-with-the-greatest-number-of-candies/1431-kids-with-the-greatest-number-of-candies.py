class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        for i,j in enumerate(candies):
            candies[i] = candies[i] + extraCandies
            if candies[i] == max(candies):
                result[i] = True
            candies[i] = candies[i] - extraCandies
        return result