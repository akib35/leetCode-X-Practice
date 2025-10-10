class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []

        for spell in spells:
            min_needed = ceil(success / spell)
            index = bisect_left(potions, min_needed)
            result.append(n - index)
        return result
