class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        max_length = 0
        current_length = 2

        for i in range(2, n):
            if nums[i] == nums[i - 1] + nums[i - 2]:
                current_length += 1
            else:
                if current_length >= 3:
                    max_length = max(max_length, current_length)
                current_length = 2

        max_length = max(max_length, current_length)

        return max_length


if __name__ == "__main__":
    s = Solution()
    print(s.longestSubarray([1, 1, 1, 1, 2, 3, 5, 1]))
    print(s.longestSubarray([1000000000, 1000000000, 1000000000]))
