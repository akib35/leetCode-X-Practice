class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_set = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            if s[right] not in temp_set:
                temp_set.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                temp_set.remove(s[left])
                left += 1
        return max_length
