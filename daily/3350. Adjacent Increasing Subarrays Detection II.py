class Solution:
    def maxIncreasingSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        inc_end = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_end[i] = inc_end[i - 1] + 1
        print(inc_end)
        inc_start = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc_start[i] = inc_start[i + 1] + 1
        print(inc_start)
        max_k = 0
        for i in range(n - 1):
            k = min(inc_end[i], inc_start[i + 1])
            max_k = max(max_k, k)

        return max_k


# Test example
s = Solution()
print(s.maxIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1]))  # Output: 3
