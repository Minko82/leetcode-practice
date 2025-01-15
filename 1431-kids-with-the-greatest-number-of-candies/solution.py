from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        # extra_candies_total = []
        # for candy in candies:
        #     extra_candies_total.append(candy + extraCandies)

        # OR YOU CAN WRITE IT LIKE:
        extra_candies_total = [candy + extraCandies for candy in candies]

        max_candies = max(candies)

        for candy in extra_candies_total:
            if candy >= max_candies:
                results.append(True)
            else:
                results.append(False)

        print(results)
        return results


# Testing the solution
sol = Solution()
sol.kidsWithCandies([2,3,5,1,3], 3)