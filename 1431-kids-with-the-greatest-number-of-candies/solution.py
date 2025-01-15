from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        extra_candies_total = [candy + extraCandies for candy in candies]
        # print (extra_candies_total)
        max_candies = max(candies)
        # print(max_candies)
        results = []
        
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