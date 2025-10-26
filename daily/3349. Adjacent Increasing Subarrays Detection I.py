class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        for i in range(n - 2 * k + 1):
            if self.isStrictlyIncreasing(nums[i : i + k]) and self.isStrictlyIncreasing(
                nums[i + k : i + 2 * k]
            ):
                return True
        return False

    def isStrictlyIncreasing(self, sub: list[int]) -> bool:
        for i in range(1, len(sub)):
            if sub[i] <= sub[i - 1]:
                return False
        return True


# Test cases
s = Solution()
print(s.hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3))  # True
print(s.hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5))  # False
